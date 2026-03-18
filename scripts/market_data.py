"""
Market Data Fetcher for Investment Research Report
"""
import yfinance as yf
import json
from datetime import datetime

def get_ticker_data(ticker):
    try:
        t = yf.Ticker(ticker)
        info = t.info
        hist = t.history(period="1y")
        
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('navPrice')
        week52_high = info.get('fiftyTwoWeekHigh')
        week52_low = info.get('fiftyTwoWeekLow')
        pe = info.get('trailingPE') or info.get('forwardPE')
        mktcap = info.get('marketCap')
        div_yield = info.get('dividendYield')
        beta = info.get('beta')
        
        if not hist.empty and len(hist) > 5:
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            one_yr_return = ((end_price - start_price) / start_price) * 100
            ytd_data = hist[hist.index.year == datetime.now().year]['Close']
            ytd_return = ((ytd_data.iloc[-1] - ytd_data.iloc[0]) / ytd_data.iloc[0]) * 100 if len(ytd_data) > 1 else None
        else:
            one_yr_return = None
            ytd_return = None
        
        return {
            'ticker': ticker,
            'name': (info.get('longName') or info.get('shortName', ticker))[:40],
            'price': round(price, 2) if price else None,
            'week52_high': round(week52_high, 2) if week52_high else None,
            'week52_low': round(week52_low, 2) if week52_low else None,
            'pe_ratio': round(pe, 2) if pe else None,
            'market_cap_B': round(mktcap / 1e9, 1) if mktcap else None,
            'dividend_yield_pct': round(div_yield * 100, 2) if div_yield else None,
            'beta': round(beta, 2) if beta else None,
            'one_yr_return_pct': round(one_yr_return, 1) if one_yr_return is not None else None,
            'ytd_return_pct': round(ytd_return, 1) if ytd_return is not None else None,
            'sector': info.get('sector'),
        }
    except Exception as e:
        return {'ticker': ticker, 'error': str(e)[:80]}

ai_stocks = ['NVDA', 'AMD', 'AVGO', 'TSM', 'ASML', 'MU', 'INTC',
             'MSFT', 'GOOGL', 'AMZN', 'META', 'ORCL',
             'PLTR', 'CRM', 'SNOW',
             'ANET', 'MRVL',
             'VST', 'CEG',
             'EQIX', 'DLR']

ai_etfs = ['QQQ', 'SMH', 'SOXX', 'XLK', 'BOTZ', 'AIQ',
           'CLOU', 'HACK', 'BUG', 'CIBR',
           'URA', 'LIT', 'COPX', 'GRID']

geo_stocks = ['XOM', 'CVX', 'COP', 'OXY', 'SLB',
              'LMT', 'RTX', 'NOC', 'GD', 'BA',
              'PANW', 'CRWD', 'FTNT',
              'MOS', 'NTR']

geo_etfs = ['XLE', 'XOP', 'OIH',
            'ITA', 'XAR', 'PPA',
            'GLD', 'IAU', 'GDX',
            'TLT', 'SHY', 'BIL',
            'DBA', 'MOO', 'REMX']

all_tickers = list(dict.fromkeys(ai_stocks + ai_etfs + geo_stocks + geo_etfs))

print(f"Fetching {len(all_tickers)} tickers...\n")
results = {}
for i, ticker in enumerate(all_tickers):
    data = get_ticker_data(ticker)
    results[ticker] = data
    status = f"${data['price']}" if data.get('price') else data.get('error','?')[:30]
    print(f"  [{i+1:>2}/{len(all_tickers)}] {ticker:<6} {status}")

with open('/home/azura/eva_investment/scripts/market_data_results.json', 'w') as f:
    json.dump({'fetched_at': datetime.now().isoformat(), 'data': results}, f, indent=2)

print("\n=== SUMMARY ===")
for group_name, tickers in [("AI Stocks", ai_stocks), ("AI ETFs", ai_etfs), ("Geo Stocks", geo_stocks), ("Geo ETFs", geo_etfs)]:
    print(f"\n--- {group_name} ---")
    print(f"{'Ticker':<7} {'Price':>8} {'1Y%':>7} {'YTD%':>7} {'52WH':>8} {'52WL':>8} {'P/E':>7} {'Beta':>6} {'MCap$B':>8}")
    for t in tickers:
        d = results.get(t, {})
        if 'error' in d:
            print(f"{t:<7} ERR: {d['error'][:50]}")
            continue
        p = f"${d['price']}" if d.get('price') else '-'
        r1y = f"{d['one_yr_return_pct']}%" if d.get('one_yr_return_pct') is not None else '-'
        ytd = f"{d['ytd_return_pct']}%" if d.get('ytd_return_pct') is not None else '-'
        h = f"${d['week52_high']}" if d.get('week52_high') else '-'
        l = f"${d['week52_low']}" if d.get('week52_low') else '-'
        pe = f"{d['pe_ratio']}" if d.get('pe_ratio') else '-'
        beta = f"{d['beta']}" if d.get('beta') else '-'
        mc = f"${d['market_cap_B']}B" if d.get('market_cap_B') else '-'
        print(f"{t:<7} {p:>8} {r1y:>7} {ytd:>7} {h:>8} {l:>8} {pe:>7} {beta:>6} {mc:>8}")
