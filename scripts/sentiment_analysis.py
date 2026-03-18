"""
Sentiment: short interest, insider transactions (from yfinance)
"""
import yfinance as yf
import pandas as pd
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')

STOCKS = ['NVDA','CEG','MSFT','LMT','TSM','AVGO','ANET','CRWD','NTR','RTX']

def get_sentiment(ticker):
    t = yf.Ticker(ticker)
    info = t.info
    result = {'ticker': ticker}
    
    result['short_pct_float'] = info.get('shortPercentOfFloat')
    result['short_ratio'] = info.get('shortRatio')
    
    # Insider transactions
    try:
        insiders = t.insider_transactions
        if insiders is not None and not insiders.empty:
            # Last 6 months
            from datetime import datetime, timedelta
            cutoff = datetime.now() - timedelta(days=180)
            # startDate column
            if 'startDate' in insiders.columns:
                recent = insiders[pd.to_datetime(insiders['startDate']) >= cutoff]
            else:
                recent = insiders.head(20)
            
            buys = 0; sells = 0; buy_val = 0; sell_val = 0
            for _, row in recent.iterrows():
                txn_type = str(row.get('transactionText','') or row.get('text','')).lower()
                shares = row.get('shares', 0) or 0
                val = row.get('value', 0) or 0
                if 'sale' in txn_type or 'sell' in txn_type or 'sold' in txn_type:
                    sells += 1; sell_val += val
                elif 'purchase' in txn_type or 'buy' in txn_type or 'acqui' in txn_type:
                    buys += 1; buy_val += val
            
            result['insider_buys_6m'] = buys
            result['insider_sells_6m'] = sells
            result['insider_buy_value'] = buy_val
            result['insider_sell_value'] = sell_val
            result['insider_sentiment'] = 'buying' if buys > sells else ('selling' if sells > buys else 'neutral')
        else:
            result['insider_buys_6m'] = result['insider_sells_6m'] = 0
            result['insider_sentiment'] = 'neutral'
    except Exception as e:
        result['insider_sentiment'] = 'N/A'
        result['insider_error'] = str(e)
    
    return result

def main():
    all_s = {}
    for ticker in STOCKS:
        try:
            r = get_sentiment(ticker)
            print(f"{ticker}: short={r.get('short_pct_float')}, insider={r.get('insider_sentiment')}")
            all_s[ticker] = r
        except Exception as e:
            print(f"ERROR {ticker}: {e}")
            all_s[ticker] = {'ticker': ticker, 'error': str(e)}
    
    out_path = '/home/azura/eva_investment/scripts/sentiment_results.json'
    with open(out_path, 'w') as f:
        json.dump(all_s, f, indent=2, default=str)
    print(f"\nSaved to {out_path}")
    return all_s

if __name__ == '__main__':
    main()
