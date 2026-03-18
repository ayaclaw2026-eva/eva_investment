"""
ETF Screener - Detailed comparison of thematic ETFs
"""
import yfinance as yf
import json
from datetime import datetime

etf_universe = {
    # AI/Tech
    'QQQ':  {'theme': 'AI/Tech Broad', 'desc': 'Nasdaq-100 ETF', 'er': 0.20},
    'XLK':  {'theme': 'AI/Tech Broad', 'desc': 'S&P 500 Technology Sector', 'er': 0.08},
    'SMH':  {'theme': 'Semiconductors', 'desc': 'VanEck Semiconductor ETF', 'er': 0.35},
    'SOXX': {'theme': 'Semiconductors', 'desc': 'iShares Semiconductor ETF', 'er': 0.35},
    'BOTZ': {'theme': 'AI/Robotics', 'desc': 'Global X Robotics & AI', 'er': 0.68},
    'AIQ':  {'theme': 'AI Broad', 'desc': 'Global X AI & Technology', 'er': 0.68},
    'ROBO': {'theme': 'AI/Robotics', 'desc': 'ROBO Global Robotics & Automation', 'er': 0.95},
    'CLOU': {'theme': 'Cloud', 'desc': 'Global X Cloud Computing', 'er': 0.68},
    'SKYY': {'theme': 'Cloud', 'desc': 'First Trust Cloud Computing', 'er': 0.60},
    'HACK': {'theme': 'Cybersecurity', 'desc': 'ETFMG Prime Cyber Security', 'er': 0.60},
    'BUG':  {'theme': 'Cybersecurity', 'desc': 'Global X Cybersecurity', 'er': 0.50},
    'CIBR': {'theme': 'Cybersecurity', 'desc': 'First Trust NASDAQ Cybersecurity', 'er': 0.60},
    'URA':  {'theme': 'Nuclear/Energy', 'desc': 'Global X Uranium ETF', 'er': 0.69},
    'GRID': {'theme': 'Power Grid', 'desc': 'First Trust NASDAQ Clean Edge Smart Grid', 'er': 0.58},
    'LIT':  {'theme': 'Materials/AI', 'desc': 'Global X Lithium & Battery Tech', 'er': 0.75},
    'COPX': {'theme': 'Materials/AI', 'desc': 'Global X Copper Miners', 'er': 0.65},
    'REMX': {'theme': 'Rare Earths', 'desc': 'VanEck Rare Earth/Strategic Metals', 'er': 0.59},
    # Geopolitical
    'XLE':  {'theme': 'Energy', 'desc': 'Energy Select Sector SPDR', 'er': 0.08},
    'XOP':  {'theme': 'E&P', 'desc': 'S&P Oil & Gas E&P ETF', 'er': 0.35},
    'OIH':  {'theme': 'Oil Services', 'desc': 'VanEck Oil Services ETF', 'er': 0.35},
    'ITA':  {'theme': 'Defense', 'desc': 'iShares US Aerospace & Defense', 'er': 0.39},
    'XAR':  {'theme': 'Defense', 'desc': 'SPDR S&P Aerospace & Defense', 'er': 0.35},
    'PPA':  {'theme': 'Defense', 'desc': 'Invesco Aerospace & Defense ETF', 'er': 0.57},
    'GLD':  {'theme': 'Safe Haven', 'desc': 'SPDR Gold Shares', 'er': 0.40},
    'IAU':  {'theme': 'Safe Haven', 'desc': 'iShares Gold Trust (lower cost)', 'er': 0.25},
    'GDX':  {'theme': 'Gold Miners', 'desc': 'VanEck Gold Miners ETF', 'er': 0.51},
    'TLT':  {'theme': 'Treasuries', 'desc': '20+ Year Treasury Bond ETF', 'er': 0.15},
    'SHY':  {'theme': 'Treasuries', 'desc': '1-3 Year Treasury Bond ETF', 'er': 0.15},
    'BIL':  {'theme': 'Cash', 'desc': 'SPDR Bloomberg 1-3 Month T-Bill', 'er': 0.14},
    'DBA':  {'theme': 'Agriculture', 'desc': 'Invesco Agriculture Fund', 'er': 0.93},
    'MOO':  {'theme': 'Agri-Business', 'desc': 'VanEck Agribusiness ETF', 'er': 0.55},
}

print("Fetching ETF data...\n")
results = []
for ticker, meta in etf_universe.items():
    t = yf.Ticker(ticker)
    try:
        info = t.info
        hist = t.history(period="1y")
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('navPrice')
        aum = info.get('totalAssets')
        avg_vol = info.get('averageVolume') or info.get('averageDailyVolume10Day')
        
        if not hist.empty and len(hist) > 5:
            r1y = ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
            ytd_d = hist[hist.index.year == datetime.now().year]['Close']
            ytd = ((ytd_d.iloc[-1] - ytd_d.iloc[0]) / ytd_d.iloc[0]) * 100 if len(ytd_d) > 1 else None
            # Volatility (annualized)
            daily_ret = hist['Close'].pct_change().dropna()
            vol_ann = daily_ret.std() * (252**0.5) * 100
        else:
            r1y = ytd = vol_ann = None
        
        results.append({
            'ticker': ticker,
            'theme': meta['theme'],
            'desc': meta['desc'],
            'er': meta['er'],
            'price': round(price, 2) if price else None,
            'aum_B': round(aum/1e9, 2) if aum else None,
            'avg_vol_M': round(avg_vol/1e6, 2) if avg_vol else None,
            '1y_return': round(r1y, 1) if r1y is not None else None,
            'ytd_return': round(ytd, 1) if ytd is not None else None,
            'ann_vol': round(vol_ann, 1) if vol_ann is not None else None,
            'sharpe_proxy': round(r1y / vol_ann, 2) if (r1y and vol_ann and vol_ann > 0) else None,
        })
        print(f"  {ticker:<5} AUM: ${round(aum/1e9,1) if aum else '?'}B | 1Y: {round(r1y,1) if r1y else '?'}% | Vol: {round(vol_ann,1) if vol_ann else '?'}%")
    except Exception as e:
        print(f"  {ticker} ERROR: {e}")
        results.append({'ticker': ticker, 'error': str(e)[:60], **meta})

# Print comparison table
print("\n" + "="*110)
print(f"{'Ticker':<6} {'Theme':<18} {'Price':>7} {'AUM$B':>7} {'ER%':>5} {'1Y%':>7} {'YTD%':>7} {'AnnVol':>8} {'Sharpe':>7}")
print("="*110)
for r in sorted(results, key=lambda x: x.get('theme','') + x.get('ticker','')):
    if 'error' in r: continue
    print(f"{r['ticker']:<6} {r['theme']:<18} {('$'+str(r['price'])) if r.get('price') else '-':>7} "
          f"{('$'+str(r['aum_B'])+'B') if r.get('aum_B') else '-':>7} "
          f"{str(r['er'])+'%':>5} "
          f"{(str(r['1y_return'])+'%') if r.get('1y_return') is not None else '-':>7} "
          f"{(str(r['ytd_return'])+'%') if r.get('ytd_return') is not None else '-':>7} "
          f"{(str(r['ann_vol'])+'%') if r.get('ann_vol') is not None else '-':>8} "
          f"{str(r['sharpe_proxy']) if r.get('sharpe_proxy') is not None else '-':>7}")

with open('/home/azura/eva_investment/scripts/etf_screener_results.json', 'w') as f:
    json.dump({'fetched_at': datetime.now().isoformat(), 'data': results}, f, indent=2)
print("\nSaved etf_screener_results.json")
