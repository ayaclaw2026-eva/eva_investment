"""
Options Hedging Strategy Analysis
For a balanced long-term investor with geopolitical + AI exposure
"""
import yfinance as yf
from datetime import datetime, timedelta
import json

def get_options_snapshot(ticker, strategy_type="hedge"):
    """Fetch options chain data for hedging analysis"""
    try:
        t = yf.Ticker(ticker)
        info = t.info
        price = info.get('currentPrice') or info.get('regularMarketPrice')
        if not price:
            return {'ticker': ticker, 'error': 'No price'}
        
        # Get available expiry dates
        expirations = t.options
        if not expirations:
            return {'ticker': ticker, 'error': 'No options'}
        
        # Find ~3 month and ~6 month expirations
        target_dates = {}
        now = datetime.now()
        for days_out, label in [(60, '2m'), (90, '3m'), (180, '6m'), (365, '12m')]:
            target = now + timedelta(days=days_out)
            closest = min(expirations, key=lambda x: abs((datetime.strptime(x, '%Y-%m-%d') - target).days))
            target_dates[label] = closest
        
        results = {
            'ticker': ticker,
            'current_price': round(price, 2),
            'strategies': {}
        }
        
        # For hedging: focus on puts (protective puts) and collars
        for label, expiry in target_dates.items():
            try:
                chain = t.option_chain(expiry)
                puts = chain.puts
                calls = chain.calls
                
                if puts.empty:
                    continue
                
                # 5% OTM put (protective put / hedge)
                otm5_strike = round(price * 0.95, 0)
                # 10% OTM put (cheaper tail hedge)
                otm10_strike = round(price * 0.90, 0)
                # ATM put
                atm_strike = round(price, 0)
                
                def find_option(df, strike):
                    if df.empty: return None
                    row = df.iloc[(df['strike'] - strike).abs().argsort()[:1]]
                    if row.empty: return None
                    r = row.iloc[0]
                    bid = r.get('bid', 0) or 0
                    ask = r.get('ask', 0) or 0
                    mid = (bid + ask) / 2 if (bid or ask) else r.get('lastPrice', 0)
                    iv = r.get('impliedVolatility', None)
                    return {
                        'strike': float(r['strike']),
                        'bid': round(float(bid), 2),
                        'ask': round(float(ask), 2),
                        'mid': round(float(mid), 2),
                        'iv': round(float(iv)*100, 1) if iv else None,
                        'oi': int(r.get('openInterest', 0) or 0),
                        'cost_pct_of_stock': round(float(mid)/price*100, 2) if mid and price else None
                    }
                
                results['strategies'][label] = {
                    'expiry': expiry,
                    'protective_put_5pct_otm': find_option(puts, otm5_strike),
                    'tail_hedge_put_10pct_otm': find_option(puts, otm10_strike),
                    'atm_put': find_option(puts, atm_strike),
                    # For collar: sell OTM call to offset put cost
                    'covered_call_5pct_otm': find_option(calls, round(price * 1.05, 0)),
                    'covered_call_10pct_otm': find_option(calls, round(price * 1.10, 0)),
                }
            except Exception as e:
                results['strategies'][label] = {'error': str(e)[:60]}
        
        return results
    except Exception as e:
        return {'ticker': ticker, 'error': str(e)[:80]}

# Key hedging targets
hedge_tickers = {
    'NVDA': 'Core AI holding — high beta, needs protection',
    'QQQ': 'Tech/AI broad hedge — portfolio level',
    'SMH': 'Semiconductor ETF hedge',
    'GLD': 'Safe haven — already a hedge, covered calls for income',
    'XLE': 'Energy/geopolitical exposure hedge',
    'ITA': 'Defense ETF — hedge against peace/de-escalation',
    'SPY': 'Broad market hedge',
    'TLT': 'Rate risk hedge — long duration bonds',
}

print("Fetching options data for hedging analysis...\n")
options_results = {}
for ticker, rationale in hedge_tickers.items():
    print(f"  {ticker}: {rationale}")
    data = get_options_snapshot(ticker)
    options_results[ticker] = {'rationale': rationale, 'data': data}
    if 'error' not in data:
        # Print key hedge metrics
        strats = data.get('strategies', {})
        for period in ['3m', '6m']:
            s = strats.get(period, {})
            if 'error' in s: continue
            p5 = s.get('protective_put_5pct_otm', {}) or {}
            p10 = s.get('tail_hedge_put_10pct_otm', {}) or {}
            cc5 = s.get('covered_call_5pct_otm', {}) or {}
            if p5:
                collar_cost = round((p5.get('mid',0) or 0) - (cc5.get('mid',0) or 0), 2)
                print(f"    [{period}] 5% OTM Put: ${p5.get('mid','N/A')} ({p5.get('cost_pct_of_stock','?')}% of stock) | IV: {p5.get('iv','?')}%")
                print(f"    [{period}] 10% OTM Put: ${p10.get('mid','N/A')} | Collar net cost: ${collar_cost}/share")
    else:
        print(f"    Error: {data['error']}")

with open('/home/azura/eva_investment/scripts/options_data.json', 'w') as f:
    json.dump({'fetched_at': datetime.now().isoformat(), 'data': options_results}, f, indent=2)

print("\nOptions data saved.")
