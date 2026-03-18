"""
DCF Engine — Full quantitative analysis for 10 stocks
"""
import yfinance as yf
import pandas as pd
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')

RF = 0.043
ERP = 0.055
STOCKS = ['NVDA', 'CEG', 'MSFT', 'LMT', 'TSM', 'AVGO', 'ANET', 'CRWD', 'NTR', 'RTX']

def compute_wacc(beta):
    if beta is None or (isinstance(beta, float) and np.isnan(beta)):
        beta = 1.0
    return RF + beta * ERP

def dcf_scenario(revenue_base, fcf_margin, growth_rates_5y, terminal_g, wacc, shares, debt, cash):
    fcfs = []
    rev = revenue_base
    for g in growth_rates_5y:
        rev = rev * (1 + g)
        fcfs.append(rev * fcf_margin)
    pv_fcf = sum(fcf / (1 + wacc)**i for i, fcf in enumerate(fcfs, 1))
    tv = fcfs[-1] * (1 + terminal_g) / (wacc - terminal_g)
    pv_tv = tv / (1 + wacc)**5
    ev = pv_fcf + pv_tv
    equity_value = ev - debt + cash
    if shares and shares > 0:
        return equity_value / shares
    return None

def reverse_dcf(current_price, fcf_margin, wacc, revenue_base, shares, debt, cash, terminal_g=0.03):
    if not all([current_price, fcf_margin, revenue_base, shares]):
        return None
    def equity_val(g):
        return dcf_scenario(revenue_base, fcf_margin, [g]*5, terminal_g, wacc, shares, debt, cash)
    lo, hi = -0.10, 1.50
    for _ in range(80):
        mid = (lo + hi) / 2
        val = equity_val(mid)
        if val is None:
            return None
        if val < current_price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def historical_pe_percentile(ticker, current_pe):
    try:
        t = yf.Ticker(ticker)
        hist = t.history(period='5y', interval='3mo')
        earnings = t.quarterly_earnings
        if earnings is None or earnings.empty:
            return None, None, None, None
        eps_series = earnings['EPS'].sort_index()
        pe_list = []
        for date, row in hist.iterrows():
            price = row['Close']
            d = date.tz_localize(None) if date.tzinfo else date
            past_eps = eps_series[eps_series.index <= d]
            if len(past_eps) >= 4:
                ttm_eps = past_eps.iloc[-4:].sum()
                if ttm_eps > 0:
                    pe_list.append(price / ttm_eps)
        if not pe_list:
            return None, None, None, None
        pe_arr = np.array(pe_list)
        pe_min = float(np.nanmin(pe_arr))
        pe_max = float(np.nanmax(pe_arr))
        pe_med = float(np.nanmedian(pe_arr))
        pct = float(np.mean(pe_arr <= current_pe) * 100) if current_pe else None
        return pe_min, pe_max, pe_med, pct
    except Exception as e:
        return None, None, None, None

def analyze_stock(ticker):
    print(f"\n{'='*50}\nAnalyzing {ticker}...")
    result = {'ticker': ticker}
    t = yf.Ticker(ticker)
    info = t.info

    price = info.get('currentPrice') or info.get('regularMarketPrice')
    mktcap = info.get('marketCap')
    pe_ttm = info.get('trailingPE')
    pe_fwd = info.get('forwardPE')
    beta = info.get('beta')
    de_ratio = info.get('debtToEquity')
    div_yield = info.get('dividendYield')
    shares = info.get('sharesOutstanding')
    total_debt = info.get('totalDebt') or 0
    total_cash = info.get('totalCash') or 0
    short_pct = info.get('shortPercentOfFloat')
    mean_target = info.get('targetMeanPrice')
    ev_ebitda = info.get('enterpriseToEbitda')
    enterprise_value = info.get('enterpriseValue')

    result.update({'price':price,'mktcap':mktcap,'pe_ttm':pe_ttm,'pe_fwd':pe_fwd,
                   'beta':beta,'de_ratio':de_ratio,'div_yield':div_yield,'shares':shares,
                   'total_debt':total_debt,'total_cash':total_cash,'short_pct':short_pct,
                   'mean_target':mean_target,'ev_ebitda':ev_ebitda,'enterprise_value':enterprise_value})

    # Revenue & FCF
    try:
        inc = t.financials
        rev = inc.loc['Total Revenue'].sort_index() if 'Total Revenue' in inc.index else None
    except:
        rev = None
    
    try:
        cf = t.cashflow
        opcf = cf.loc['Operating Cash Flow'].sort_index() if 'Operating Cash Flow' in cf.index else None
        capex = cf.loc['Capital Expenditure'].sort_index() if 'Capital Expenditure' in cf.index else None
        fcf = opcf + capex if opcf is not None and capex is not None else None
    except:
        fcf = None

    if rev is not None:
        rv = rev.dropna()
        result['revenue_history'] = {str(d.year): float(v) for d, v in rv.items()}
        rv_vals = rv.values
        result['rev_latest'] = float(rv_vals[-1]) if len(rv_vals) else None
        result['rev_cagr_5y'] = float((rv_vals[-1]/rv_vals[0])**(1/max(len(rv_vals)-1,1))-1) if len(rv_vals)>=2 else None
    else:
        result['revenue_history'] = {}; result['rev_latest'] = None; result['rev_cagr_5y'] = None

    if fcf is not None:
        fcf_clean = fcf.dropna()
        result['fcf_history'] = {str(d.year): float(v) for d, v in fcf_clean.items()}
        if rev is not None and len(fcf_clean) > 0:
            rv2 = rev.dropna()
            common = fcf_clean.index.intersection(rv2.index)
            if len(common) > 0:
                margins = [fcf_clean[d]/rv2[d] for d in common if rv2[d] > 0]
                result['fcf_margin_avg'] = float(np.mean(margins)) if margins else None
            else:
                result['fcf_margin_avg'] = None
        else:
            result['fcf_margin_avg'] = None
    else:
        result['fcf_history'] = {}; result['fcf_margin_avg'] = None

    # Margins
    try:
        inc2 = t.financials
        if 'Gross Profit' in inc2.index and 'Total Revenue' in inc2.index:
            gp = inc2.loc['Gross Profit'].sort_index().dropna()
            rv3 = inc2.loc['Total Revenue'].sort_index().dropna()
            common = gp.index.intersection(rv3.index)
            result['gross_margin_history'] = {str(d.year): float(gp[d]/rv3[d]) for d in common if rv3[d]>0}
        if 'EBIT' in inc2.index and 'Total Revenue' in inc2.index:
            eb = inc2.loc['EBIT'].sort_index().dropna()
            rv4 = inc2.loc['Total Revenue'].sort_index().dropna()
            common2 = eb.index.intersection(rv4.index)
            result['op_margin_history'] = {str(d.year): float(eb[d]/rv4[d]) for d in common2 if rv4[d]>0}
    except:
        result['gross_margin_history'] = {}; result['op_margin_history'] = {}

    # EPS history
    try:
        earn = t.earnings
        if earn is not None and not earn.empty and 'EPS' in earn.columns:
            eps_v = earn['EPS'].dropna()
            result['eps_history'] = {str(y): float(v) for y,v in eps_v.items()}
            eps_vals = eps_v.values
            if len(eps_vals)>=2 and eps_vals[0]!=0:
                result['eps_cagr_5y'] = float((abs(eps_vals[-1])/abs(eps_vals[0]))**(1/(len(eps_vals)-1))-1)
            else:
                result['eps_cagr_5y'] = None
        else:
            result['eps_history'] = {}; result['eps_cagr_5y'] = None
    except:
        result['eps_history'] = {}; result['eps_cagr_5y'] = None

    # Analyst consensus
    try:
        recs = t.recommendations_summary
        if recs is not None and not recs.empty:
            latest = recs.iloc[0]
            result['analyst_buy'] = int(latest.get('strongBuy',0)) + int(latest.get('buy',0))
            result['analyst_hold'] = int(latest.get('hold',0))
            result['analyst_sell'] = int(latest.get('sell',0)) + int(latest.get('strongSell',0))
        else:
            result['analyst_buy'] = result['analyst_hold'] = result['analyst_sell'] = None
    except:
        result['analyst_buy'] = result['analyst_hold'] = result['analyst_sell'] = None

    # Historical P/E
    pe_min, pe_max, pe_med, pe_pct = historical_pe_percentile(ticker, pe_ttm)
    result.update({'pe_5y_min':pe_min,'pe_5y_max':pe_max,'pe_5y_median':pe_med,'pe_current_pct':pe_pct})

    # 52-week
    try:
        h52 = t.history(period='1y')
        if not h52.empty and price:
            lo52 = float(h52['Low'].min())
            hi52 = float(h52['High'].max())
            result['pct_52w'] = (price-lo52)/(hi52-lo52)*100 if hi52>lo52 else None
            result['lo52'] = lo52; result['hi52'] = hi52
        else:
            result['pct_52w'] = result['lo52'] = result['hi52'] = None
    except:
        result['pct_52w'] = result['lo52'] = result['hi52'] = None

    # WACC & DCF
    wacc = compute_wacc(beta)
    result['wacc'] = wacc

    rev_base = result['rev_latest']
    fcf_m = result['fcf_margin_avg']
    rev_cagr = result['rev_cagr_5y']

    if rev_base and fcf_m and shares and price:
        base_g = max(min(rev_cagr if rev_cagr else 0.05, 0.60), 0.01)
        bull_g = min(base_g * 1.35, 0.70)
        bear_g = max(base_g * 0.50, 0.01)

        def taper(g):
            return [g, g*0.88, g*0.76, g*0.65, g*0.55]

        scenarios_def = {
            'bear': {'gs': taper(bear_g), 'terminal_g': 0.02, 'fcf_m': max(fcf_m*0.85, 0.001)},
            'base': {'gs': taper(base_g), 'terminal_g': 0.03, 'fcf_m': fcf_m},
            'bull': {'gs': taper(bull_g), 'terminal_g': 0.04, 'fcf_m': min(fcf_m*1.15, 0.60)},
        }
        result['scenarios'] = {}
        for nm, sc in scenarios_def.items():
            iv = dcf_scenario(rev_base, sc['fcf_m'], sc['gs'], sc['terminal_g'], wacc, shares, total_debt, total_cash)
            updown = (iv/price-1)*100 if iv and price else None
            result['scenarios'][nm] = {
                'growth_schedule': [round(g,4) for g in sc['gs']],
                'fcf_margin': round(sc['fcf_m'],4),
                'terminal_g': sc['terminal_g'],
                'intrinsic_per_share': round(iv,2) if iv else None,
                'upside_pct': round(updown,1) if updown is not None else None
            }
        rev_g = reverse_dcf(price, fcf_m, wacc, rev_base, shares, total_debt, total_cash)
        result['reverse_dcf_implied_growth'] = round(rev_g,4) if rev_g is not None else None
    else:
        result['scenarios'] = {}
        result['reverse_dcf_implied_growth'] = None

    # PEG
    eps_cagr = result.get('eps_cagr_5y')
    if pe_fwd and eps_cagr and eps_cagr > 0:
        result['peg'] = round(pe_fwd / (eps_cagr * 100), 3)
    else:
        result['peg'] = None

    print(f"  Price={price} | WACC={wacc:.1%} | RevCAGR={rev_cagr}")
    for nm, sc in result['scenarios'].items():
        print(f"  {nm.upper()}: IV=${sc['intrinsic_per_share']} ({sc['upside_pct']}%)")
    print(f"  Reverse DCF implied growth: {result['reverse_dcf_implied_growth']}")

    return result

def main():
    all_results = {}
    for ticker in STOCKS:
        try:
            r = analyze_stock(ticker)
            all_results[ticker] = r
        except Exception as e:
            print(f"ERROR {ticker}: {e}")
            import traceback; traceback.print_exc()
            all_results[ticker] = {'ticker': ticker, 'error': str(e)}
    
    out_path = '/home/azura/eva_investment/scripts/dcf_results.json'
    with open(out_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nSaved to {out_path}")
    return all_results

if __name__ == '__main__':
    main()
