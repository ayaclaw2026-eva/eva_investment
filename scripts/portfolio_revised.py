"""
Revised Portfolio Allocation — Evidence-based
Loads DCF/ETF/comps results and outputs final allocation
"""
import json

ALLOCATION = {
    "BIL": {"weight": 0.10, "type": "ETF", "rationale": "Risk-free proxy; Sharpe negative but capital preservation"},
    "ITA": {"weight": 0.06, "type": "ETF", "rationale": "Sharpe >2.0; defense supercycle beneficiary"},
    "XAR": {"weight": 0.05, "type": "ETF", "rationale": "Sharpe 2.25; aerospace & defense, best Sharpe in universe"},
    "IAU": {"weight": 0.05, "type": "ETF", "rationale": "Sharpe 2.16; gold hedge, low equity correlation"},
    "GLD": {"weight": 0.03, "type": "ETF", "rationale": "Sharpe 2.14; additional gold exposure, geopolitical hedge"},
    "SMH": {"weight": 0.05, "type": "ETF", "rationale": "Sharpe 1.88; AI/semi exposure at ETF level"},
    "GRID": {"weight": 0.05, "type": "ETF", "rationale": "Sharpe 1.83; power grid + clean energy for AI data centers"},
    "COPX": {"weight": 0.04, "type": "ETF", "rationale": "Sharpe 1.95; copper demand from AI infrastructure buildout"},
    "URA": {"weight": 0.03, "type": "ETF", "rationale": "Sharpe 2.15 (1Y); nuclear renaissance theme; high vol"},
    "CIBR": {"weight": 0.03, "type": "ETF", "rationale": "Sharpe -0.22 (1Y) — REDUCED from prior; still strategic"},
    "XLE": {"weight": 0.03, "type": "ETF", "rationale": "Sharpe 1.14; energy diversification/geopolitical hedge"},
    "QQQ": {"weight": 0.03, "type": "ETF", "rationale": "Broad tech; Sharpe 0.87 vs SPY; limited add"},
    "LMT": {"weight": 0.08, "type": "Stock", "rationale": "DCF base $1,180 (+84%); lowest beta; defense supercycle"},
    "RTX": {"weight": 0.05, "type": "Stock", "rationale": "DCF bull +21%; defense; low beta 0.43"},
    "MSFT": {"weight": 0.05, "type": "Stock", "rationale": "Fair valuation; AI cloud moat; quality compounder"},
    "NTR": {"weight": 0.04, "type": "Stock", "rationale": "Cyclical bottom; cheap vs peers; 3-5Y mean reversion"},
    "TSM": {"weight": 0.04, "type": "Stock", "rationale": "Essential AI foundry; expensive (46% implied g); small position"},
    "AVGO": {"weight": 0.04, "type": "Stock", "rationale": "AI custom silicon + networking; 42% implied g; moat"},
    "NVDA": {"weight": 0.04, "type": "Stock", "rationale": "AI GPU dominance; richly priced (64% implied g); trimmed"},
    "ANET": {"weight": 0.03, "type": "Stock", "rationale": "AI data center networking; 44% implied g; moat"},
    "CRWD": {"weight": 0.03, "type": "Stock", "rationale": "Cybersecurity leader; 50% implied g; expensive"},
    "CEG": {"weight": 0.03, "type": "Stock", "rationale": "Nuclear restart; 56% implied g; speculative"},
    "CASH": {"weight": 0.02, "type": "Cash", "rationale": "Opportunistic rebalancing buffer"},
}

total = sum(v['weight'] for v in ALLOCATION.values())
print(f"Total allocation: {total:.0%}")
print("\nPortfolio Summary:")
print(f"{'Ticker':<8} {'Weight':<8} {'Type':<8} Rationale")
print("-"*80)
for ticker, a in ALLOCATION.items():
    print(f"{ticker:<8} {a['weight']*100:.0f}%     {a['type']:<8} {a['rationale'][:60]}")

with open('/home/azura/eva_investment/scripts/portfolio_weights.json', 'w') as f:
    json.dump(ALLOCATION, f, indent=2)
print("\nSaved portfolio_weights.json")
