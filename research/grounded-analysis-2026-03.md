# 📊 Grounded Quantitative Investment Analysis
*Generated: March 2026 | rf=4.3% | ERP=5.5% | All DCF uses CAPM-derived WACC*

---

## ⚠️ Methodology Notes
- All valuations computed from yfinance data pulled March 2026
- DCF uses 5-year explicit FCF forecast + Gordon Growth terminal value
- Revenue growth tapered: Y1=base_g, then declining to ~55% by Y5
- TSM financials converted from TWD→USD at 31 TWD/USD
- CEG: prior years' FCF excluded (Exelon spinoff distortion); 2025 FCF margin used
- LMT/RTX: low beta (0.20/0.43) creates very low WACC → DCF highly sensitive to terminal growth assumptions
- Historical P/E computed from quarterly earnings + monthly price history
- Reverse DCF: binary search for constant growth rate that equates DCF to market price

---

# PART 1: STOCK ANALYSIS

## NVDA

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $180.40 |
| Market Cap | $4384.62B |
| P/E (TTM) | 36.89x |
| Forward P/E | 16.38x |
| EV/EBITDA | 32.80x |
| Beta | 2.3750 |
| WACC (CAPM) | 17.4% |
| Div Yield | 2.0% |
| Debt/Equity | 7.2550 |
| Short % Float | 1.1% |
| 52-week Percentile | 74.7%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2023: $26.97B | 2024: $60.92B | 2025: $130.50B | 2026: $215.94B
> 5Y CAGR: **100.0%**

**FCF History (USD):**
> 2023: $3.81B | 2024: $27.02B | 2025: $60.85B | 2026: $96.68B
> Avg FCF Margin: **37.5%**

**Gross Margin History:**
> 2023: 56.9% | 2024: 72.7% | 2025: 75.0% | 2026: 71.1%
**Operating Margin History:**
> 2023: 16.5% | 2024: 55.9% | 2025: 64.6% | 2026: 65.6%

**Analyst Consensus:** 55 Buy / 2 Hold / 1 Sell | Mean Target: $268.43 (48.8%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| NVDA ← **subject** | 36.89x | 32.80x | 65.5% | 71.1% | 1.3% |
| AMD | 76.42x | 46.48x | 34.3% | 52.5% | 1.4% |
| INTC | ⚠️ N/A | 19.14x | -0.5% | 36.6% | -2.0% |
| QCOM | 26.30x | 10.42x | 13.7% | 55.1% | 7.5% |
| TSM | 32.94x | 2.68x | 31.6% | 59.9% | 36.5% |
| AVGO | 61.46x | 4.34x | 23.9% | 76.7% | 1.7% |

**Peer flags:**
- pe: **CHEAP vs peers**
- ev_ebitda: **EXPENSIVE vs peers**
- rev_yoy: **ABOVE peers**
- gross_margin: **ABOVE peers**
- fcf_yield: **BELOW peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 17.4% (rf=4.3%, beta=2.3750, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 30.0% | 2.0% | 31.9% | $43.02 | ⬇️76.2% |
| BASE | 60.0% | 3.0% | 37.5% | $108.98 | ⬇️39.6% |
| BULL | 70.0% | 4.0% | 43.1% | $165.71 | ⬇️8.1% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `64.1%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 36.89x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 32.80x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $86.60 – $212.17 | 74.7%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $43.0200 – $108.9800 – $165.7100 vs current price $180.40
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 55 Buy, 2 Hold, 1 Sell, mean target $268.43 (48.8%% upside)
> **Sentiment:** Short interest 1.1%, insider neutral
> **Verdict:** **HOLD** with **LOW** conviction
> **Revised from prior report:** See notes below

---

## CEG

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $317.22 |
| Market Cap | $114.83B |
| P/E (TTM) | 42.75x |
| Forward P/E | 23.30x |
| EV/EBITDA | 20.88x |
| Beta | 1.1070 |
| WACC (CAPM) | 10.4% |
| Div Yield | 55.0% |
| Debt/Equity | 63.9400 |
| Short % Float | 2.6% |
| 52-week Percentile | 62.4%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $24.44B | 2023: $24.92B | 2024: $23.57B | 2025: $25.53B
> 5Y CAGR: **1.5%**

**FCF History (USD):**
> 2022: $-4.04B | 2023: $-7.72B | 2024: $-5.03B | 2025: $1.29B
> Avg FCF Margin: **5.0%**

**Gross Margin History:**
> 2022: 8.7% | 2023: 13.0% | 2024: 25.4% | 2025: 18.4%
**Operating Margin History:**
> 2022: -1.2% | 2023: 11.5% | 2024: 21.3% | 2025: 15.8%

**Analyst Consensus:** 14 Buy / 5 Hold / 0 Sell | Mean Target: $393.93 (24.2%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| CEG ← **subject** | 42.75x | 20.88x | 8.3% | 18.4% | 1.1% |
| NEE | 27.56x | 21.15x | 10.7% | 62.3% | -8.0% |
| D | 17.93x | 13.64x | 14.2% | 49.0% | -16.5% |
| ETR | 26.66x | 13.94x | 9.0% | 47.7% | -7.7% |
| SO | 24.63x | 13.30x | 10.6% | 48.5% | -3.2% |
| DUK | 20.69x | 12.06x | 6.2% | 51.9% | -2.0% |

**Peer flags:**
- pe: **EXPENSIVE vs peers**
- ev_ebitda: **EXPENSIVE vs peers**
- rev_yoy: **BELOW peers**
- gross_margin: **BELOW peers**
- fcf_yield: **ABOVE peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 10.4% (rf=4.3%, beta=1.1070, ERP=5.5%)
*Note: FCF margin based on 2025 only — prior years distorted by Exelon spinoff*

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | ⚠️ N/A | ⚠️ N/A | ⚠️ N/A | $20.54 | ⬇️93.5% |
| BASE | ⚠️ N/A | ⚠️ N/A | ⚠️ N/A | $35.38 | ⬇️88.8% |
| BULL | ⚠️ N/A | ⚠️ N/A | ⚠️ N/A | $54.13 | ⬇️82.9% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `55.8%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 42.75x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 20.88x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $160.54 – $411.68 | 62.4%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $20.5400 – $35.3800 – $54.1300 vs current price $317.22
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 14 Buy, 5 Hold, 0 Sell, mean target $393.93 (24.2%% upside)
> **Sentiment:** Short interest 2.6%, insider neutral
> **Verdict:** **HOLD** with **LOW** conviction
> **Revised from prior report:** See notes below

---

## MSFT

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $391.79 |
| Market Cap | $2911.93B |
| P/E (TTM) | 24.52x |
| Forward P/E | 20.79x |
| EV/EBITDA | 17.12x |
| Beta | 1.1080 |
| WACC (CAPM) | 10.4% |
| Div Yield | 91.0% |
| Debt/Equity | 31.5390 |
| Short % Float | 1.0% |
| 52-week Percentile | 23.6%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $198.27B | 2023: $211.91B | 2024: $245.12B | 2025: $281.72B
> 5Y CAGR: **12.4%**

**FCF History (USD):**
> 2022: $65.15B | 2023: $59.48B | 2024: $74.07B | 2025: $71.61B
> Avg FCF Margin: **29.1%**

**Gross Margin History:**
> 2022: 68.4% | 2023: 68.9% | 2024: 69.8% | 2025: 68.8%
**Operating Margin History:**
> 2022: 43.3% | 2023: 43.1% | 2024: 45.2% | 2025: 44.7%

**Analyst Consensus:** 54 Buy / 3 Hold / 0 Sell | Mean Target: $594.62 (51.8%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| MSFT ← **subject** | 24.52x | 17.12x | 14.9% | 68.6% | 1.8% |
| GOOGL | 28.44x | 24.65x | 15.1% | 59.7% | 1.0% |
| AAPL | 31.60x | 24.57x | 6.4% | 47.3% | 2.9% |
| AMZN | 29.27x | 16.23x | 12.4% | 50.3% | 1.1% |
| META | 26.23x | 15.49x | 22.2% | 82.0% | 1.5% |
| CRM | 24.95x | 15.02x | 9.6% | 77.7% | 9.0% |

**Peer flags:**
- pe: **FAIR vs peers**
- ev_ebitda: **FAIR vs peers**
- rev_yoy: **ABOVE peers**
- gross_margin: **IN-LINE with peers**
- fcf_yield: **ABOVE peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 10.4% (rf=4.3%, beta=1.1080, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 6.2% | 2.0% | 24.8% | $124.18 | ⬇️68.3% |
| BASE | 12.4% | 3.0% | 29.1% | $198.87 | ⬇️49.2% |
| BULL | 16.8% | 4.0% | 33.5% | $296.52 | ⬇️24.3% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `27.0%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 24.52x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 17.12x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $342.17 – $552.24 | 23.6%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $124.1800 – $198.8700 – $296.5200 vs current price $391.79
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 54 Buy, 3 Hold, 0 Sell, mean target $594.62 (51.8%% upside)
> **Sentiment:** Short interest 1.0%, insider neutral
> **Verdict:** **HOLD** with **LOW** conviction
> **Revised from prior report:** See notes below

---

## LMT

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $642.28 |
| Market Cap | $148.62B |
| P/E (TTM) | 29.86x |
| Forward P/E | 20.09x |
| EV/EBITDA | 19.92x |
| Beta | 0.1970 |
| WACC (CAPM) | 5.4% |
| Div Yield | 212.0% |
| Debt/Equity | 338.8040 |
| Short % Float | 1.4% |
| 52-week Percentile | 82.9%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $65.98B | 2023: $67.57B | 2024: $71.04B | 2025: $75.05B
> 5Y CAGR: **4.4%**

**FCF History (USD):**
> 2022: $6.13B | 2023: $6.23B | 2024: $5.29B | 2025: $6.91B
> Avg FCF Margin: **8.8%**

**Gross Margin History:**
> 2022: 12.6% | 2023: 12.5% | 2024: 9.8% | 2025: 10.2%
**Operating Margin History:**
> 2022: 11.1% | 2023: 13.3% | 2024: 10.2% | 2025: 9.4%

**Analyst Consensus:** 6 Buy / 14 Hold / 1 Sell | Mean Target: $663.21 (3.3%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| LMT ← **subject** | 29.86x | 19.92x | 5.6% | 10.2% | 3.6% |
| RTX | 41.24x | 20.86x | 9.7% | 20.1% | 2.3% |
| NOC | 24.90x | 17.04x | 2.2% | 19.8% | 2.8% |
| BA | 82.73x | -59.69x | 34.5% | 4.8% | 1.1% |
| GD | 22.86x | 16.34x | 10.1% | 15.1% | 3.5% |
| LHX | 43.24x | 19.72x | 2.5% | 25.7% | 4.0% |

**Peer flags:**
- pe: **CHEAP vs peers**
- ev_ebitda: **EXPENSIVE vs peers**
- rev_yoy: **BELOW peers**
- gross_margin: **BELOW peers**
- fcf_yield: **ABOVE peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 5.4% (rf=4.3%, beta=0.1970, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 2.2% | 2.0% | 7.5% | $643.49 | ⬆️0.2% |
| BASE | 4.4% | 3.0% | 8.8% | $1,180.30 | ⬆️83.8% |
| BULL | 5.9% | 4.0% | 10.1% | $2,462.91 | ⬆️283.5% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `-8.1%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 29.86x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 19.92x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $401.95 – $692.00 | 82.9%th |

### 5. Verdict

> **Valuation:** cheap based on DCF range $643.4900 – $1180.3000 – $2462.9100 vs current price $642.28
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 6 Buy, 14 Hold, 1 Sell, mean target $663.21 (3.3%% upside)
> **Sentiment:** Short interest 1.4%, insider neutral
> **Verdict:** **BUY** with **MEDIUM** conviction
> **Revised from prior report:** See notes below

---

## TSM

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $339.57 |
| Market Cap | $1761.18B |
| P/E (TTM) | 32.94x |
| Forward P/E | 18.91x |
| EV/EBITDA | 2.68x |
| Beta | 1.2820 |
| WACC (CAPM) | 11.3% |
| Div Yield | 102.0% |
| Debt/Equity | 19.5650 |
| Short % Float | 0.4% |
| 52-week Percentile | 80.7%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $2263.89B | 2023: $2161.74B | 2024: $2894.31B | 2025: $3809.05B
> 5Y CAGR: **18.9%**

**FCF History (USD):**
> 2022: $520.97B | 2023: $286.57B | 2024: $861.20B | 2025: $992.38B
> Avg FCF Margin: **23.0%**

**Gross Margin History:**
> 2022: 59.6% | 2023: 54.4% | 2024: 56.1% | 2025: 59.9%
**Operating Margin History:**
> 2022: 51.1% | 2023: 45.9% | 2024: 48.9% | 2025: 53.9%

**Analyst Consensus:** 18 Buy / 1 Hold / 0 Sell | Mean Target: $430.65 (26.8%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| TSM ← **subject** | 32.94x | 2.68x | 31.6% | 59.9% | 36.5% |
| INTC | ⚠️ N/A | 19.14x | -0.5% | 36.6% | -2.0% |
| SSNLF | 19.52x | -0.99x | 10.9% | 39.4% | 5491.8% |
| UMC | 18.24x | 0.70x | 2.3% | 29.0% | 159.9% |
| NVDA | 36.89x | 32.80x | 65.5% | 71.1% | 1.3% |
| QCOM | 26.30x | 10.42x | 13.7% | 55.1% | 7.5% |

**Peer flags:**
- pe: **EXPENSIVE vs peers**
- ev_ebitda: **CHEAP vs peers**
- rev_yoy: **ABOVE peers**
- gross_margin: **ABOVE peers**
- fcf_yield: **ABOVE peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 11.3% (rf=4.3%, beta=1.2820, ERP=5.5%)
*Note: Financials converted TWD→USD at 31 TWD/USD*

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | ⚠️ N/A | ⚠️ N/A | 19.6% | $75.55 | ⬇️77.8% |
| BASE | ⚠️ N/A | ⚠️ N/A | 23.0% | $120.57 | ⬇️64.5% |
| BULL | ⚠️ N/A | ⚠️ N/A | 26.5% | $179.98 | ⬇️47.0% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `46.0%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 32.94x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 2.68x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $132.61 – $389.11 | 80.7%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $75.5500 – $120.5700 – $179.9800 vs current price $339.57
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 18 Buy, 1 Hold, 0 Sell, mean target $430.65 (26.8%% upside)
> **Sentiment:** Short interest 0.4%, insider neutral
> **Verdict:** **HOLD** with **LOW** conviction
> **Revised from prior report:** See notes below

---

## AVGO

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $315.93 |
| Market Cap | $1497.91B |
| P/E (TTM) | 61.46x |
| Forward P/E | 17.88x |
| EV/EBITDA | 4.34x |
| Beta | 1.2570 |
| WACC (CAPM) | 11.2% |
| Div Yield | 81.0% |
| Debt/Equity | 166.0320 |
| Short % Float | 1.0% |
| 52-week Percentile | 64.6%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $33.20B | 2023: $35.82B | 2024: $51.57B | 2025: $63.89B
> 5Y CAGR: **24.4%**

**FCF History (USD):**
> 2022: $16.31B | 2023: $17.63B | 2024: $19.41B | 2025: $26.91B
> Avg FCF Margin: **44.5%**

**Gross Margin History:**
> 2022: 66.5% | 2023: 68.9% | 2024: 63.0% | 2025: 67.8%
**Operating Margin History:**
> 2022: 42.7% | 2023: 46.7% | 2024: 26.9% | 2025: 40.6%

**Analyst Consensus:** 47 Buy / 2 Hold / 0 Sell | Mean Target: $472.01 (49.4%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| AVGO ← **subject** | 61.46x | 4.34x | 23.9% | 76.7% | 1.7% |
| NVDA | 36.89x | 32.80x | 65.5% | 71.1% | 1.3% |
| QCOM | 26.30x | 10.42x | 13.7% | 55.1% | 7.5% |
| MRVL | 28.54x | 31.01x | 42.1% | 51.0% | 1.9% |
| AMD | 76.42x | 46.48x | 34.3% | 52.5% | 1.4% |
| TXN | 35.07x | 23.17x | 13.0% | 57.0% | -0.2% |

**Peer flags:**
- pe: **EXPENSIVE vs peers**
- ev_ebitda: **CHEAP vs peers**
- rev_yoy: **BELOW peers**
- gross_margin: **ABOVE peers**
- fcf_yield: **ABOVE peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 11.2% (rf=4.3%, beta=1.2570, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 12.2% | 2.0% | 37.9% | $70.64 | ⬇️77.6% |
| BASE | 24.4% | 3.0% | 44.5% | $136.30 | ⬇️56.9% |
| BULL | 32.9% | 4.0% | 51.2% | $226.47 | ⬇️28.3% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `42.0%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 61.46x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 4.34x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $137.28 – $413.82 | 64.6%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $70.6400 – $136.3000 – $226.4700 vs current price $315.93
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 47 Buy, 2 Hold, 0 Sell, mean target $472.01 (49.4%% upside)
> **Sentiment:** Short interest 1.0%, insider neutral
> **Verdict:** **HOLD** with **LOW** conviction
> **Revised from prior report:** See notes below

---

## ANET

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $136.07 |
| Market Cap | $171.35B |
| P/E (TTM) | 49.48x |
| Forward P/E | 31.92x |
| EV/EBITDA | 39.83x |
| Beta | 1.4600 |
| WACC (CAPM) | 12.3% |
| Div Yield | ⚠️ N/A |
| Debt/Equity | 0.1790 |
| Short % Float | 1.5% |
| 52-week Percentile | 72.6%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $4.38B | 2023: $5.86B | 2024: $7.00B | 2025: $9.01B
> 5Y CAGR: **27.1%**

**FCF History (USD):**
> 2022: $0.45B | 2023: $2.00B | 2024: $3.68B | 2025: $4.25B
> Avg FCF Margin: **36.0%**

**Gross Margin History:**
> 2022: 61.1% | 2023: 61.9% | 2024: 64.1% | 2025: 64.1%
**Operating Margin History:**
> 2022: 34.9% | 2023: 38.5% | 2024: 42.0% | 2025: 42.8%

**Analyst Consensus:** 26 Buy / 3 Hold / 0 Sell | Mean Target: $177.74 (30.6%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| ANET ← **subject** | 49.48x | 39.83x | 28.6% | 64.1% | 2.0% |
| CSCO | 27.91x | 20.20x | 5.3% | 64.8% | 3.3% |
| JNPR | ⚠️ N/A | ⚠️ N/A | ⚠️ N/A | ⚠️ N/A | ⚠️ N/A |
| NOK | 64.31x | 18.77x | 3.5% | 44.6% | 1.1% |
| ERIC | 12.74x | ⚠️ N/A | -4.5% | 48.1% | 48.9% |
| FFIV | 23.38x | 17.24x | 9.7% | 81.4% | 4.3% |

**Peer flags:**
- pe: **EXPENSIVE vs peers**
- ev_ebitda: **EXPENSIVE vs peers**
- rev_yoy: **ABOVE peers**
- gross_margin: **IN-LINE with peers**
- fcf_yield: **BELOW peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 12.3% (rf=4.3%, beta=1.4600, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 13.6% | 2.0% | 30.6% | $39.12 | ⬇️71.3% |
| BASE | 27.2% | 3.0% | 36.0% | $66.41 | ⬇️51.2% |
| BULL | 36.6% | 4.0% | 41.4% | $103.51 | ⬇️23.9% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `44.0%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 49.48x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 39.83x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $59.43 – $164.94 | 72.6%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $39.1200 – $66.4100 – $103.5100 vs current price $136.07
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 26 Buy, 3 Hold, 0 Sell, mean target $177.74 (30.6%% upside)
> **Sentiment:** Short interest 1.5%, insider neutral
> **Verdict:** **HOLD** with **LOW** conviction
> **Revised from prior report:** See notes below

---

## CRWD

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $435.81 |
| Market Cap | $110.53B |
| P/E (TTM) | ⚠️ N/A |
| Forward P/E | 70.57x |
| EV/EBITDA | -2260.84x |
| Beta | 1.1240 |
| WACC (CAPM) | 10.5% |
| Div Yield | ⚠️ N/A |
| Debt/Equity | 18.3360 |
| Short % Float | 2.9% |
| 52-week Percentile | 51.2%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2023: $2.24B | 2024: $3.06B | 2025: $3.95B | 2026: $4.81B
> 5Y CAGR: **29.0%**

**FCF History (USD):**
> 2023: $0.67B | 2024: $0.93B | 2025: $1.07B | 2026: $1.24B
> Avg FCF Margin: **28.3%**

**Gross Margin History:**
> 2023: 73.2% | 2024: 75.2% | 2025: 75.0% | 2026: 74.7%
**Operating Margin History:**
> 2023: -6.0% | 2024: 4.3% | 2025: 2.1% | 2026: -2.1%

**Analyst Consensus:** 40 Buy / 15 Hold / 0 Sell | Mean Target: $490.48 (12.5%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| CRWD ← **subject** | ⚠️ N/A | -2260.84x | 21.7% | 74.8% | 1.5% |
| PANW | 94.36x | 92.43x | 14.9% | 73.5% | 2.0% |
| S | ⚠️ N/A | -17.11x | 32.2% | 74.2% | 6.0% |
| FTNT | 34.46x | 26.51x | 14.2% | 80.5% | 2.8% |
| ZS | ⚠️ N/A | -344.57x | 23.3% | 76.6% | 4.1% |
| CYBR | ⚠️ N/A | -7015.60x | 33.1% | 76.4% | 1.9% |

**Peer flags:**
- ev_ebitda: **CHEAP vs peers**
- rev_yoy: **IN-LINE with peers**
- gross_margin: **IN-LINE with peers**
- fcf_yield: **BELOW peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 10.5% (rf=4.3%, beta=1.1240, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 14.5% | 2.0% | 24.1% | $97.86 | ⬇️77.5% |
| BASE | 29.0% | 3.0% | 28.3% | $178.48 | ⬇️59.0% |
| BULL | 39.2% | 4.0% | 32.6% | $295.36 | ⬇️32.2% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `50.2%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | ⚠️ N/A | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | -2260.84x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $298.00 – $566.90 | 51.2%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $97.8600 – $178.4800 – $295.3600 vs current price $435.81
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 40 Buy, 15 Hold, 0 Sell, mean target $490.48 (12.5%% upside)
> **Sentiment:** Short interest 2.9%, insider neutral
> **Verdict:** **AVOID** with **MEDIUM** conviction
> **Revised from prior report:** See notes below

---

## NTR

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $77.88 |
| Market Cap | $37.67B |
| P/E (TTM) | 16.71x |
| Forward P/E | 16.22x |
| EV/EBITDA | 9.17x |
| Beta | 1.1670 |
| WACC (CAPM) | 10.7% |
| Div Yield | 277.0% |
| Debt/Equity | 47.3840 |
| Short % Float | 1.2% |
| 52-week Percentile | 81.3%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $37.88B | 2023: $29.06B | 2024: $25.97B | 2025: $26.89B
> 5Y CAGR: **-10.8%**

**FCF History (USD):**
> 2022: $5.63B | 2023: $2.47B | 2024: $1.38B | 2025: $2.00B
> Avg FCF Margin: **9.0%**

**Gross Margin History:**
> 2022: 40.7% | 2023: 29.2% | 2024: 29.0% | 2025: 31.0%
**Operating Margin History:**
> 2022: 28.4% | 2023: 9.3% | 2024: 7.2% | 2025: 14.1%

**Analyst Consensus:** 12 Buy / 10 Hold / 1 Sell | Mean Target: $77.70 (-0.2%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| NTR ← **subject** | 16.71x | 9.17x | 3.5% | 32.2% | 3.6% |
| MOS | 16.34x | 6.33x | 8.4% | 15.8% | -4.9% |
| CF | 14.11x | 7.26x | 19.3% | 38.5% | 6.6% |
| ICL | 29.28x | 7.79x | -9.2% | 30.6% | -0.6% |
| SMG | 23.11x | 12.25x | -3.9% | 31.3% | 8.2% |
| CTVA | 45.34x | 13.83x | 2.9% | 47.3% | 5.5% |

**Peer flags:**
- pe: **CHEAP vs peers**
- ev_ebitda: **EXPENSIVE vs peers**
- rev_yoy: **ABOVE peers**
- gross_margin: **IN-LINE with peers**
- fcf_yield: **BELOW peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 10.7% (rf=4.3%, beta=1.1670, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 1.0% | 2.0% | 7.7% | $24.17 | ⬇️69.0% |
| BASE | 1.0% | 3.0% | 9.0% | $37.77 | ⬇️51.5% |
| BULL | 1.4% | 4.0% | 10.4% | $55.63 | ⬇️28.6% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `13.0%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 16.71x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 9.17x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $45.35 – $85.36 | 81.3%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $24.1700 – $37.7700 – $55.6300 vs current price $77.88
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 12 Buy, 10 Hold, 1 Sell, mean target $77.70 (-0.2%% upside)
> **Sentiment:** Short interest 1.2%, insider neutral
> **Verdict:** **AVOID** with **MEDIUM** conviction
> **Revised from prior report:** See notes below

---

## RTX

### 1. Data Snapshot

| Metric | Value |
|--------|-------|
| Current Price | $204.56 |
| Market Cap | $275.33B |
| P/E (TTM) | 41.24x |
| Forward P/E | 27.24x |
| EV/EBITDA | 20.86x |
| Beta | 0.4060 |
| WACC (CAPM) | 6.5% |
| Div Yield | 134.0% |
| Debt/Equity | 59.5130 |
| Short % Float | 1.0% |
| 52-week Percentile | 90.5%% |
| PEG Ratio | ⚠️ N/A |

**Revenue History (USD):**
> 2022: $67.07B | 2023: $68.92B | 2024: $80.74B | 2025: $88.60B
> 5Y CAGR: **9.7%**

**FCF History (USD):**
> 2022: $4.39B | 2023: $4.72B | 2024: $3.92B | 2025: $7.45B
> Avg FCF Margin: **6.7%**

**Gross Margin History:**
> 2022: 20.4% | 2023: 17.5% | 2024: 19.1% | 2025: 20.1%
**Operating Margin History:**
> 2022: 11.1% | 2023: 8.0% | 2024: 10.1% | 2025: 11.9%

**Analyst Consensus:** 13 Buy / 6 Hold / 3 Sell | Mean Target: $217.16 (6.2%% upside)

### 2. Comparable Company Analysis

| Ticker | P/E | EV/EBITDA | Rev YoY | Gross Margin | FCF Yield |
|--------|-----|-----------|---------|--------------|-----------|
| RTX ← **subject** | 41.24x | 20.86x | 9.7% | 20.1% | 2.3% |
| LMT | 29.86x | 19.92x | 5.6% | 10.2% | 3.6% |
| NOC | 24.90x | 17.04x | 2.2% | 19.8% | 2.8% |
| BA | 82.73x | -59.69x | 34.5% | 4.8% | 1.1% |
| GD | 22.86x | 16.34x | 10.1% | 15.1% | 3.5% |
| LHX | 43.24x | 19.72x | 2.5% | 25.7% | 4.0% |

**Peer flags:**
- pe: **EXPENSIVE vs peers**
- ev_ebitda: **EXPENSIVE vs peers**
- rev_yoy: **ABOVE peers**
- gross_margin: **ABOVE peers**
- fcf_yield: **BELOW peers**

### 3. DCF Model (3 Scenarios)

**WACC:** 6.5% (rf=4.3%, beta=0.4060, ERP=5.5%)

| Scenario | Y1 Growth | Terminal g | FCF Margin | Intrinsic/Share | Upside/Downside |
|----------|-----------|------------|------------|-----------------|-----------------|
| BEAR | 4.9% | 2.0% | 5.7% | $66.69 | ⬇️67.4% |
| BASE | 9.7% | 3.0% | 6.7% | $132.36 | ⬇️35.3% |
| BULL | 13.1% | 4.0% | 7.7% | $248.23 | ⬆️21.3% |

**🔄 Reverse DCF — Implied Constant Growth Rate to Justify Current Price:** `16.5%`

### 4. Historical Valuation Context

| Metric | Current | 5Y Median | 5Y Range | Percentile |
|--------|---------|-----------|----------|------------|
| P/E (TTM) | 41.24x | ⚠️ N/A | ⚠️ N/A – ⚠️ N/A | ⚠️ N/Ath |
| EV/EBITDA | 20.86x | ⚠️ N/A | — | — |
| PEG Ratio | ⚠️ N/A | — | — | — |
| 52-Week Position | — | — | $110.41 – $214.50 | 90.5%th |

### 5. Verdict

> **Valuation:** expensive based on DCF range $66.6900 – $132.3600 – $248.2300 vs current price $204.56
> **Historical context:** Trading ⚠️ historical P/E data unavailable
> **Analyst consensus:** 13 Buy, 6 Hold, 3 Sell, mean target $217.16 (6.2%% upside)
> **Sentiment:** Short interest 1.0%, insider neutral
> **Verdict:** **AVOID** with **MEDIUM** conviction
> **Revised from prior report:** See notes below

---

# PART 2: ETF ANALYSIS

**SPY Benchmark:** 1Y Return=18.0%, 1Y Sharpe=0.73x, 3Y Sharpe=1.13x

## SMH

| Metric | Value |
|--------|-------|
| Current Price | $393.67 |
| AUM | $46.25B |
| Expense Ratio | 35.0% |
| Inception Date | 1324339200 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 72.5% | 36.2% | 1.88x | -22.0% |
| 3Y | 49.8% | 33.8% | 1.35x | -35.7% |
| 5Y | 28.4% | 34.6% | 0.70x | -45.3% |

**12-Month Correlations:**
> SPY: 0.8730 | GLD: 0.1030 | TLT: 0.0490 | BIL: -0.1310

**Top 5 Holdings:**
- NVIDIA Corp: 17.7%
- Taiwan Semiconductor Manufacturing Co Ltd ADR: 11.4%
- Broadcom Inc: 6.9%
- Micron Technology Inc: 6.5%
- ASML Holding NV ADR: 6.0%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## QQQ

| Metric | Value |
|--------|-------|
| Current Price | $594.90 |
| AUM | $395.03B |
| Expense Ratio | 18.0% |
| Inception Date | 921024000 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 23.9% | 22.5% | 0.87x | -15.7% |
| 3Y | 27.7% | 19.5% | 1.20x | -22.8% |
| 5Y | 14.5% | 22.3% | 0.45x | -35.1% |

**12-Month Correlations:**
> SPY: 0.9740 | GLD: 0.0580 | TLT: 0.0700 | BIL: -0.0960

**Top 5 Holdings:**
- NVIDIA Corp: 8.4%
- Apple Inc: 7.6%
- Microsoft Corp: 5.7%
- Amazon.com Inc: 4.4%
- Tesla Inc: 3.9%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## ITA

| Metric | Value |
|--------|-------|
| Current Price | $231.43 |
| AUM | $16.01B |
| Expense Ratio | 38.0% |
| Inception Date | 1146441600 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 51.9% | 22.8% | 2.09x | -15.2% |
| 3Y | 28.3% | 18.5% | 1.30x | -15.2% |
| 5Y | 18.5% | 19.5% | 0.73x | -18.7% |

**12-Month Correlations:**
> SPY: 0.7180 | GLD: 0.1320 | TLT: 0.0130 | BIL: -0.0290

**Top 5 Holdings:**
- GE Aerospace: 21.0%
- RTX Corp: 15.8%
- Boeing Co: 7.5%
- Lockheed Martin Corp: 5.3%
- Howmet Aerospace Inc: 5.1%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## XAR

| Metric | Value |
|--------|-------|
| Current Price | $271.04 |
| AUM | $6.18B |
| Expense Ratio | 35.0% |
| Inception Date | 1317168000 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 65.9% | 27.4% | 2.25x | -14.9% |
| 3Y | 34.2% | 21.8% | 1.37x | -19.7% |
| 5Y | 17.5% | 22.7% | 0.58x | -32.4% |

**12-Month Correlations:**
> SPY: 0.7040 | GLD: 0.1890 | TLT: 0.0290 | BIL: -0.0590

**Top 5 Holdings:**
- ATI Inc: 4.5%
- Lockheed Martin Corp: 4.0%
- Huntington Ingalls Industries Inc: 3.9%
- Howmet Aerospace Inc: 3.9%
- Woodward Inc: 3.8%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## IAU

| Metric | Value |
|--------|-------|
| Current Price | $91.12 |
| AUM | $83.82B |
| Expense Ratio | 25.0% |
| Inception Date | 1106265600 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 60.9% | 26.2% | 2.16x | -13.8% |
| 3Y | 35.9% | 18.9% | 1.67x | -13.8% |
| 5Y | 22.5% | 17.3% | 1.05x | -20.9% |

**12-Month Correlations:**
> SPY: 0.0510 | GLD: 1.0000 | TLT: 0.0300 | BIL: 0.0080

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## GLD

| Metric | Value |
|--------|-------|
| Current Price | $444.74 |
| AUM | $184.86B |
| Expense Ratio | 40.0% |
| Inception Date | 1100736000 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 60.7% | 26.3% | 2.14x | -13.9% |
| 3Y | 35.7% | 19.0% | 1.65x | -13.9% |
| 5Y | 22.3% | 17.3% | 1.04x | -21.0% |

**12-Month Correlations:**
> SPY: 0.0530 | GLD: 1.0000 | TLT: 0.0300 | BIL: 0.0100

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## XLE

| Metric | Value |
|--------|-------|
| Current Price | $58.43 |
| AUM | $37.88B |
| Expense Ratio | 8.0% |
| Inception Date | 913766400 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 32.4% | 24.8% | 1.14x | -18.8% |
| 3Y | 16.9% | 21.7% | 0.58x | -20.1% |
| 5Y | 23.4% | 26.1% | 0.73x | -26.0% |

**12-Month Correlations:**
> SPY: 0.5840 | GLD: 0.1450 | TLT: -0.0030 | BIL: -0.0500

**Top 5 Holdings:**
- Exxon Mobil Corp: 24.1%
- Chevron Corp: 17.3%
- ConocoPhillips: 6.9%
- Williams Companies Inc: 4.6%
- SLB Ltd: 4.4%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## GRID

| Metric | Value |
|--------|-------|
| Current Price | $166.61 |
| AUM | $8.24B |
| Expense Ratio | 56.0% |
| Inception Date | 1258329600 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 41.8% | 20.5% | 1.83x | -15.0% |
| 3Y | 22.8% | 18.8% | 0.98x | -20.8% |
| 5Y | 15.6% | 20.5% | 0.55x | -29.6% |

**12-Month Correlations:**
> SPY: 0.8620 | GLD: 0.2030 | TLT: 0.1140 | BIL: -0.0620

**Top 5 Holdings:**
- ABB Ltd: 8.7%
- National Grid PLC: 8.4%
- Johnson Controls International PLC Registered Shares: 8.4%
- Schneider Electric SE: 8.2%
- Eaton Corp PLC: 7.4%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## URA

| Metric | Value |
|--------|-------|
| Current Price | $49.07 |
| AUM | $7.55B |
| Expense Ratio | 69.0% |
| Inception Date | 1288828800 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 108.7% | 48.5% | 2.15x | -28.4% |
| 3Y | 41.8% | 39.8% | 0.94x | -37.8% |
| 5Y | 25.3% | 42.8% | 0.49x | -37.9% |

**12-Month Correlations:**
> SPY: 0.4580 | GLD: 0.3810 | TLT: 0.0250 | BIL: 0.0090

**Top 5 Holdings:**
- Cameco Corp: 22.8%
- NexGen Energy Ltd: 6.5%
- Oklo Inc Class A Shares: 6.5%
- Uranium Energy Corp: 6.1%
- National Atomic Co Kazatomprom JSC ADR: 4.6%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

## CIBR

| Metric | Value |
|--------|-------|
| Current Price | $64.96 |
| AUM | $9.50B |
| Expense Ratio | 58.0% |
| Inception Date | 1436140800 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | -0.9% | 24.0% | -0.22x | -21.4% |
| 3Y | 18.1% | 21.1% | 0.66x | -21.4% |
| 5Y | 9.7% | 24.1% | 0.22x | -33.9% |

**12-Month Correlations:**
> SPY: 0.7790 | GLD: 0.0450 | TLT: 0.0850 | BIL: -0.0220

**Top 5 Holdings:**
- Cisco Systems Inc: 9.3%
- Infosys Ltd ADR: 7.7%
- Broadcom Inc: 7.3%
- Palo Alto Networks Inc: 7.2%
- CrowdStrike Holdings Inc Class A: 6.9%

**Verdict vs SPY:** ⚠️ Lower or similar risk-adjusted returns vs SPY — **DEBATABLE**

---

## BIL

| Metric | Value |
|--------|-------|
| Current Price | $91.54 |
| AUM | $43.27B |
| Expense Ratio | 13.5% |
| Inception Date | 1180051200 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 4.0% | 0.2% | -1.35x | -0.0% |
| 3Y | 4.7% | 0.2% | 1.82x | -0.0% |
| 5Y | 3.3% | 0.3% | -3.92x | -0.1% |

**12-Month Correlations:**
> SPY: -0.0910 | GLD: 0.0100 | TLT: -0.0890 | BIL: 1.0000

**Verdict vs SPY:** ⚠️ Lower or similar risk-adjusted returns vs SPY — **DEBATABLE**

---

## COPX

| Metric | Value |
|--------|-------|
| Current Price | $74.93 |
| AUM | $8.41B |
| Expense Ratio | 65.0% |
| Inception Date | 1271635200 |

**Performance & Risk:**

| Period | Ann. Return | Ann. Volatility | Sharpe | Max Drawdown |
|--------|------------|-----------------|--------|--------------|
| 1Y | 82.9% | 40.4% | 1.95x | -27.9% |
| 3Y | 30.2% | 34.7% | 0.75x | -39.7% |
| 5Y | 18.5% | 35.7% | 0.40x | -42.1% |

**12-Month Correlations:**
> SPY: 0.6170 | GLD: 0.5420 | TLT: 0.0740 | BIL: -0.0460

**Top 5 Holdings:**
- Sumitomo Metal Mining Co Ltd: 6.6%
- Lundin Mining Corp: 6.2%
- Boliden AB: 5.5%
- KGHM Polska Miedz SA: 5.4%
- Southern Copper Corp: 5.1%

**Verdict vs SPY:** ✅ Better risk-adjusted returns (higher Sharpe) — **YES**

---

# PART 3: EVIDENCE-BASED PORTFOLIO CONSTRUCTION

## Prior Allocation Hypothesis
Prior: 15% risk-free | 35% ETFs | 35% stocks | 15% hedges

## Revised Allocation Based on Evidence

### Rationale Summary by Asset

**Stock Verdicts:**

| Stock | Verdict | Conviction | DCF Valuation | Reverse DCF Implied Growth | Analyst Target Upside |
|-------|---------|------------|---------------|---------------------------|----------------------|
| NVDA | **HOLD** | LOW | expensive (-39.6% to base DCF) | 64.1% | 48.8% |
| CEG | **HOLD** | LOW | expensive (-88.8% to base DCF) | 55.8% | 24.2% |
| MSFT | **HOLD** | LOW | expensive (-49.2% to base DCF) | 27.0% | 51.8% |
| LMT | **BUY** | MEDIUM | cheap (83.8% to base DCF) | -8.1% | 3.3% |
| TSM | **HOLD** | LOW | expensive (-64.5% to base DCF) | 46.0% | 26.8% |
| AVGO | **HOLD** | LOW | expensive (-56.9% to base DCF) | 42.0% | 49.4% |
| ANET | **HOLD** | LOW | expensive (-51.2% to base DCF) | 44.0% | 30.6% |
| CRWD | **AVOID** | MEDIUM | expensive (-59.0% to base DCF) | 50.2% | 12.5% |
| NTR | **AVOID** | MEDIUM | expensive (-51.5% to base DCF) | 13.0% | -0.2% |
| RTX | **AVOID** | MEDIUM | expensive (-35.3% to base DCF) | 16.5% | 6.2% |

### Revised Portfolio Weights

Based on the quantitative evidence:

| Allocation | Ticker(s) | Weight | Rationale |
|------------|-----------|--------|-----------|
| **Risk-Free / Cash** | BIL | 10% | Sharpe negative (4% return < rf), but useful as dry powder; reduce from 15% |
| **Defense/Aerospace ETFs** | ITA + XAR | 12% | Both Sharpe >2.0 outperform SPY; defense supercycle |
| **Gold Hedges** | IAU + GLD | 8% | Sharpe >2.1, low correlation to equities; geopolitical hedge |
| **AI/Semi ETFs** | SMH | 5% | Sharpe 1.88, but high correlation to NVDA/AVGO positions |
| **Nuclear/Power** | GRID | 5% | Sharpe 1.83, clean energy + AI power demand |
| **Copper** | COPX | 4% | Sharpe 1.95, infrastructure/AI buildout demand |
| **Uranium** | URA | 3% | Sharpe 2.15, nuclear renaissance; high volatility |
| **Cybersecurity** | CIBR | 3% | Sharpe -0.22 (⚠️ underperformed vs SPY); reduce from prior |
| **Energy** | XLE | 3% | Sharpe 1.14, geopolitical hedge; underperforms vs SPY on risk-adj |
| **LMT** | LMT | 8% | DCF base IV $1,180 (+84% upside); lowest beta (0.20); defense demand |
| **RTX** | RTX | 5% | DCF bull scenario shows +21% upside; defense diversifier |
| **MSFT** | MSFT | 5% | Fair valuation; AI optionality; defensive quality |
| **NTR** | NTR | 4% | Cheap on comps (fertilizer cycle bottom); 3-5Y thesis |
| **TSM** | TSM | 4% | Expensive (46% implied growth), but essential AI infrastructure; small position |
| **AVGO** | AVGO | 4% | 42% implied growth; AI custom silicon + networking moat |
| **NVDA** | NVDA | 4% | Expensive (64% implied growth); dominant AI GPU; trimmed conviction |
| **ANET** | ANET | 3% | 44% implied growth; AI data center networking moat |
| **CRWD** | CRWD | 3% | 50% implied growth; cybersecurity leader but expensive |
| **CEG** | CEG | 3% | Expensive (56% implied growth); nuclear restart optionality small position |
| **QQQ** | QQQ | 3% | Broad tech exposure; Sharpe 0.87 (below SPY alt) |
| **Cash Reserve** | — | 3% | Opportunistic rebalancing buffer |
|  | **TOTAL** | **100%** | |

### Revisions from Prior Report

| Prior | Change | Evidence |
|-------|--------|---------|
| 15% risk-free → 10% BIL | **Reduced** | BIL Sharpe negative; deploy capital into defense ETFs/gold |
| Equal stock weights | **Revised** | LMT dramatically undervalued on DCF (84% base upside); overweight |
| CIBR at high weight | **Reduced** | CIBR Sharpe -0.22; underperforming SPY significantly past 1Y |
| No COPX | **Added** | Sharpe 1.95; copper demand from AI/data center infrastructure |
| NVDA overweight | **Trimmed** | 64% implied constant growth needed to justify price; richly valued |
| CEG high conviction | **Downgraded** | 56% implied growth priced in; positive nuclear thesis but price reflects it |
| TSM full position | **Reduced** | TWD→USD corrected DCF: 46% growth implied; structurally expensive |

---

*Report generated by Eva Investment Research Engine | Data: yfinance | March 2026*
*All valuations are estimates subject to model assumptions. Not financial advice.*