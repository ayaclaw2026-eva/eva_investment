#!/usr/bin/env python3
"""Fetch live market data using history(period='2d') for accurate 1D change."""
import yfinance as yf, json, datetime

TICKERS = [
    'AAPL','NVDA','MSFT','LMT','TSM','AVGO','ANET','MU','AMD','CEG',
    'RTX','XAR','ITA','IAU','GLD','SMH','QQQ','SPY','XLE','COPX',
    'GRID','BIL','CIBR','GOOGL','META','AMZN','URA','NTR','CRWD','CIBR'
]

def fetch():
    out = {}
    for t in TICKERS:
        try:
            tk = yf.Ticker(t)
            hist = tk.history(period='2d')
            info = tk.fast_info
            if len(hist) >= 2:
                prev = hist['Close'].iloc[-2]
                last = hist['Close'].iloc[-1]
                chg1d = round((last / prev - 1) * 100, 2)
            else:
                last = info.last_price
                chg1d = 0.0
            out[t] = {
                'price':   round(float(last), 2),
                'chg1d':   chg1d,
                'mktcap':  getattr(info, 'market_cap', None),
                'pe':      getattr(info, 'price_to_book', None),  # fallback
                'beta':    getattr(info, 'beta', None),
            }
            # Try richer info from .info (slower but more fields)
            try:
                ri = tk.info
                out[t].update({
                    'pe':         ri.get('trailingPE'),
                    'target':     ri.get('targetMeanPrice'),
                    'short_pct':  ri.get('shortPercentOfFloat'),
                    'beta':       ri.get('beta'),
                    'sector':     ri.get('sector'),
                    'mktcap':     ri.get('marketCap'),
                })
            except Exception:
                pass
        except Exception as e:
            out[t] = {'error': str(e)}
    return out

if __name__ == '__main__':
    data = fetch()
    out_path = '/home/azura/eva_investment/scripts/market_data_results.json'
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} tickers to {out_path}")
    for t, d in list(data.items())[:5]:
        if 'price' in d:
            print(f"  {t}: ${d['price']} ({d['chg1d']:+.2f}%)")
