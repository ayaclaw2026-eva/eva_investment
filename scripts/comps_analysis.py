"""
Comparable Company Analysis for 10 stocks
"""
import yfinance as yf
import pandas as pd
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')

PEERS = {
    'NVDA': ['AMD', 'INTC', 'QCOM', 'TSM', 'AVGO'],
    'CEG': ['NEE', 'D', 'ETR', 'SO', 'DUK'],
    'MSFT': ['GOOGL', 'AAPL', 'AMZN', 'META', 'CRM'],
    'LMT': ['RTX', 'NOC', 'BA', 'GD', 'LHX'],
    'TSM': ['INTC', 'SSNLF', 'UMC', 'NVDA', 'QCOM'],
    'AVGO': ['NVDA', 'QCOM', 'MRVL', 'AMD', 'TXN'],
    'ANET': ['CSCO', 'JNPR', 'NOK', 'ERIC', 'FFIV'],
    'CRWD': ['PANW', 'S', 'FTNT', 'ZS', 'CYBR'],
    'NTR': ['MOS', 'CF', 'ICL', 'SMG', 'CTVA'],
    'RTX': ['LMT', 'NOC', 'BA', 'GD', 'LHX'],
}

def get_comps_metrics(ticker):
    t = yf.Ticker(ticker)
    info = t.info
    
    pe = info.get('trailingPE')
    ev_ebitda = info.get('enterpriseToEbitda')
    
    # Revenue growth YoY
    try:
        inc = t.financials
        if 'Total Revenue' in inc.index:
            rv = inc.loc['Total Revenue'].sort_index().dropna()
            if len(rv) >= 2:
                rev_yoy = float((rv.iloc[-1] - rv.iloc[-2]) / abs(rv.iloc[-2]))
            else:
                rev_yoy = None
        else:
            rev_yoy = None
    except:
        rev_yoy = None
    
    # Gross margin
    try:
        gm = info.get('grossMargins')
    except:
        gm = None
    
    # FCF yield
    try:
        mktcap = info.get('marketCap')
        fcf = info.get('freeCashflow')
        fcf_yield = fcf / mktcap if fcf and mktcap and mktcap > 0 else None
    except:
        fcf_yield = None
    
    return {
        'ticker': ticker,
        'pe': pe,
        'ev_ebitda': ev_ebitda,
        'rev_yoy': rev_yoy,
        'gross_margin': gm,
        'fcf_yield': fcf_yield,
    }

def compare(subject, peers):
    all_tickers = [subject] + peers
    metrics = []
    for t in all_tickers:
        print(f"  Fetching {t}...")
        try:
            m = get_comps_metrics(t)
        except Exception as e:
            m = {'ticker': t, 'error': str(e)}
        metrics.append(m)
    
    df = pd.DataFrame(metrics).set_index('ticker')
    
    # Flag cheap/expensive
    subj = df.loc[subject] if subject in df.index else None
    flags = {}
    if subj is not None:
        for col in ['pe', 'ev_ebitda']:
            peer_vals = df.loc[peers, col].dropna() if peers else pd.Series()
            if not peer_vals.empty and subj[col] is not None and not np.isnan(subj[col]):
                median_peer = peer_vals.median()
                if subj[col] < median_peer * 0.85:
                    flags[col] = 'CHEAP vs peers'
                elif subj[col] > median_peer * 1.15:
                    flags[col] = 'EXPENSIVE vs peers'
                else:
                    flags[col] = 'FAIR vs peers'
        for col in ['rev_yoy', 'gross_margin', 'fcf_yield']:
            peer_vals = df.loc[peers, col].dropna() if peers else pd.Series()
            if not peer_vals.empty and subj[col] is not None and not np.isnan(subj[col]):
                median_peer = peer_vals.median()
                if subj[col] > median_peer * 1.15:
                    flags[col] = 'ABOVE peers'
                elif subj[col] < median_peer * 0.85:
                    flags[col] = 'BELOW peers'
                else:
                    flags[col] = 'IN-LINE with peers'
    
    return df.reset_index().to_dict('records'), flags

def main():
    all_comps = {}
    for subject, peers in PEERS.items():
        print(f"\n=== {subject} comps ===")
        try:
            records, flags = compare(subject, peers)
            all_comps[subject] = {'data': records, 'flags': flags}
        except Exception as e:
            print(f"ERROR: {e}")
            all_comps[subject] = {'error': str(e)}
    
    out_path = '/home/azura/eva_investment/scripts/comps_results.json'
    with open(out_path, 'w') as f:
        json.dump(all_comps, f, indent=2, default=str)
    print(f"\nSaved to {out_path}")
    return all_comps

if __name__ == '__main__':
    main()
