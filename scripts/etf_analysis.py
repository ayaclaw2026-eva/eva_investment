"""
ETF Analysis — returns, volatility, Sharpe, drawdown, correlations
"""
import yfinance as yf
import pandas as pd
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')

ETFS = ['SMH','QQQ','ITA','XAR','IAU','GLD','XLE','GRID','URA','CIBR','BIL','COPX']
RF_DAILY = 0.043 / 252

def get_returns(ticker, period='5y'):
    t = yf.Ticker(ticker)
    hist = t.history(period=period)
    if hist.empty:
        return None
    return hist['Close'].pct_change().dropna()

def annualized_return(returns, periods=252):
    total = (1 + returns).prod()
    n_years = len(returns) / periods
    return float(total ** (1/n_years) - 1) if n_years > 0 else None

def annualized_vol(returns, periods=252):
    return float(returns.std() * np.sqrt(periods))

def sharpe(returns, rf_annual=0.043, periods=252):
    ann_ret = annualized_return(returns)
    ann_vol = annualized_vol(returns)
    if ann_ret is None or ann_vol == 0:
        return None
    return float((ann_ret - rf_annual) / ann_vol)

def max_drawdown(returns):
    cum = (1 + returns).cumprod()
    roll_max = cum.cummax()
    dd = (cum - roll_max) / roll_max
    return float(dd.min())

def analyze_etf(ticker):
    print(f"  Analyzing {ticker}...")
    t = yf.Ticker(ticker)
    info = t.info
    result = {'ticker': ticker}

    result['price'] = info.get('regularMarketPrice') or info.get('navPrice')
    result['aum'] = info.get('totalAssets')
    result['expense_ratio'] = info.get('annualReportExpenseRatio') or info.get('netExpenseRatio')
    result['inception_date'] = str(info.get('fundInceptionDate', 'N/A'))

    # Top 5 holdings
    try:
        holdings = t.funds_data.top_holdings
        if holdings is not None and not holdings.empty:
            top5 = holdings.head(5)
            result['top5_holdings'] = top5.reset_index().to_dict('records')
        else:
            result['top5_holdings'] = []
    except:
        result['top5_holdings'] = []

    # Returns & risk metrics
    rets_5y = get_returns(ticker, '5y')
    
    for label, days in [('1y', 252), ('3y', 756), ('5y', 1260)]:
        if rets_5y is not None and len(rets_5y) >= days * 0.7:
            r = rets_5y.iloc[-days:]
            result[f'ann_return_{label}'] = annualized_return(r)
            result[f'ann_vol_{label}'] = annualized_vol(r)
            result[f'sharpe_{label}'] = sharpe(r)
            result[f'max_drawdown_{label}'] = max_drawdown(r)
        else:
            # try shorter period
            rets_short = get_returns(ticker, label)
            if rets_short is not None and len(rets_short) > 20:
                result[f'ann_return_{label}'] = annualized_return(rets_short)
                result[f'ann_vol_{label}'] = annualized_vol(rets_short)
                result[f'sharpe_{label}'] = sharpe(rets_short)
                result[f'max_drawdown_{label}'] = max_drawdown(rets_short)
            else:
                result[f'ann_return_{label}'] = result[f'ann_vol_{label}'] = result[f'sharpe_{label}'] = result[f'max_drawdown_{label}'] = None

    # Correlations with SPY, GLD, TLT, BIL
    benchmarks = ['SPY', 'GLD', 'TLT', 'BIL']
    corr_results = {}
    if rets_5y is not None:
        r12 = rets_5y.iloc[-252:] if len(rets_5y) >= 252 else rets_5y
        for bm in benchmarks:
            try:
                bm_ret = get_returns(bm, '1y')
                if bm_ret is not None and len(bm_ret) > 20:
                    common = r12.index.intersection(bm_ret.index)
                    if len(common) > 20:
                        corr = float(r12[common].corr(bm_ret[common]))
                        corr_results[bm] = round(corr, 3)
                    else:
                        corr_results[bm] = None
                else:
                    corr_results[bm] = None
            except:
                corr_results[bm] = None
    result['correlations_12m'] = corr_results
    
    print(f"    {ticker}: 1Y={result.get('ann_return_1y',None):.1%} Sharpe1Y={result.get('sharpe_1y',None)}")
    return result

def main():
    all_etfs = {}
    
    # Also get SPY for comparison
    spy_rets = get_returns('SPY', '5y')
    spy_metrics = {}
    if spy_rets is not None:
        for label, days in [('1y',252),('3y',756),('5y',1260)]:
            r = spy_rets.iloc[-days:]
            spy_metrics[f'sharpe_{label}'] = sharpe(r)
            spy_metrics[f'ann_return_{label}'] = annualized_return(r)
        all_etfs['SPY_benchmark'] = spy_metrics
    
    for ticker in ETFS:
        try:
            r = analyze_etf(ticker)
            all_etfs[ticker] = r
        except Exception as e:
            print(f"ERROR {ticker}: {e}")
            all_etfs[ticker] = {'ticker': ticker, 'error': str(e)}
    
    out_path = '/home/azura/eva_investment/scripts/etf_results.json'
    with open(out_path, 'w') as f:
        json.dump(all_etfs, f, indent=2, default=str)
    print(f"\nSaved to {out_path}")
    return all_etfs

if __name__ == '__main__':
    main()
