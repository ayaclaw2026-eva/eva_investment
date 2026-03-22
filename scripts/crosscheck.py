#!/usr/bin/env python3
"""
Cross-check: yfinance vs stockanalysis.com
Flags discrepancies above defined thresholds.
"""
import yfinance as yf
import urllib.request, re, json, time

TICKERS = ['NVDA','AAPL','MSFT','LMT','TSM','AVGO','ANET','MU','AMD','CEG','RTX']

THRESHOLDS = {
    'pe_ttm': 1.5,
    'pe_fwd': 4.0,
    'beta':   0.15,
    'target': 0.08,
}

def fetch_sa(ticker):
    url = f'https://stockanalysis.com/stocks/{ticker.lower()}/'
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8','ignore')
        pairs = dict(re.findall(r'>([^<>]{2,30})</td><td[^>]+>([^<>]{1,40})</td>', html))
        def num(key):
            v = pairs.get(key,'')
            m = re.search(r'[\d.]+', v)
            return float(m.group()) if m else None
        return {
            'pe_ttm': num('PE Ratio'),
            'pe_fwd': num('Forward PE'),
            'beta':   num('Beta'),
            'target': num('Price Target'),
        }
    except Exception as e:
        return {'error': str(e)}

def fetch_yf(ticker):
    tk = yf.Ticker(ticker)
    hist = tk.history(period='2d')
    ri = tk.info
    price = round(hist['Close'].iloc[-1], 2) if len(hist) >= 2 else None
    return {
        'price':  price,
        'pe_ttm': ri.get('trailingPE'),
        'pe_fwd': ri.get('forwardPE'),
        'beta':   ri.get('beta'),
        'target': ri.get('targetMeanPrice'),
    }

all_results = {}

print("=" * 68)
print("DATA CROSS-CHECK  —  yfinance  vs  stockanalysis.com")
print(f"Run: {__import__('datetime').datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
print("=" * 68)

for t in TICKERS:
    print(f"\n{'─'*50}\n📊 {t}")
    yfd = fetch_yf(t)
    time.sleep(0.5)
    sad = fetch_sa(t)

    if 'error' in sad:
        print(f"  ⚠️  stockanalysis unavailable: {sad['error']}")
        all_results[t] = {'status': 'fetch_error'}
        continue

    issues = []
    fields = [
        ('pe_ttm', 'P/E TTM',    'x',  THRESHOLDS['pe_ttm'], False),
        ('pe_fwd', 'P/E Fwd*',   'x',  THRESHOLDS['pe_fwd'], False),
        ('beta',   'Beta',       '',   THRESHOLDS['beta'],   False),
        ('target', 'Ana. Target','$',  THRESHOLDS['target'], True),
    ]

    for key, label, unit, thresh, relative in fields:
        yv = yfd.get(key)
        sv = sad.get(key)
        if yv is None and sv is None:
            print(f"  ➖ {label:<14}: both N/A")
            continue
        if yv is None or sv is None:
            print(f"  ⚠️  {label:<14}: yfinance={yv}  SA={sv}  (one source missing)")
            continue
        gap = abs(yv-sv)/sv if relative else abs(yv-sv)
        flag = gap > thresh
        icon = "❌" if flag else "✅"
        gap_str = f"{gap*100:.1f}%" if relative else f"{gap:.2f}{unit}"
        print(f"  {icon} {label:<14}: yf={yv:.2f}{unit}  SA={sv:.2f}{unit}  diff={gap_str}")
        if flag:
            issues.append(f"{label} diff={gap_str}")

    if issues:
        print(f"  🚨 FLAG: {', '.join(issues)}")
        all_results[t] = {'status':'discrepancy','issues':issues,'yf':yfd,'sa':sad}
    else:
        print(f"  ✅ All within tolerance")
        all_results[t] = {'status':'ok','yf':yfd,'sa':sad}

print("\n" + "=" * 68)
ok   = [t for t,r in all_results.items() if r.get('status')=='ok']
disc = [t for t,r in all_results.items() if r.get('status')=='discrepancy']
err  = [t for t,r in all_results.items() if r.get('status')=='fetch_error']
print(f"✅ Within tolerance : {ok}")
print(f"❌ Flag for review  : {disc}")
print(f"⚠️  Fetch error      : {err}")

with open('/home/azura/.openclaw/workspace/crosscheck_results.json','w') as f:
    json.dump(all_results, f, indent=2, default=str)
print("Saved to crosscheck_results.json")
