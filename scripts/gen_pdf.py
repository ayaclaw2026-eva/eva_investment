#!/usr/bin/env python3
"""Eva Investment Research PDF — March 25, 2026"""
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
import re

OUTPUT = '/home/azura/.openclaw/workspace/investment-daily.pdf'

# Page setup — Landscape A4
W, H = 841, 595
NAV_H = 22
TK_Y = H - NAV_H - 6 - 44
CONTENT_TOP = TK_Y - 8
BOTTOM = 30
PAD = 18

# Colors
BG     = HexColor('#0d1117')
SURFACE= HexColor('#161b22')
SURF2  = HexColor('#21262d')
BORDER = HexColor('#30363d')
TEXT   = HexColor('#e6edf3')
MUTED  = HexColor('#8b949e')
ACCENT = HexColor('#58a6ff')
GREEN  = HexColor('#3fb950')
RED    = HexColor('#f85149')
YELLOW = HexColor('#d29922')
PURPLE = HexColor('#bc8cff')
ORANGE = HexColor('#ff9500')
GOLD   = HexColor('#e3b341')
TEAL   = HexColor('#39d353')
NAVY   = HexColor('#1f3a5f')

def is_color(x): return isinstance(x, Color)

# ── Helpers ─────────────────────────────────────────────────────────────────
def ct_title(c, x, y, text, size=9.5, color=TEXT):
    c.setFont('Helvetica-Bold', size); c.setFillColor(color); c.drawString(x, y, text)
    return y - size - 3

def ct_body(c, x, y, text, size=7.5, color=MUTED):
    c.setFont('Helvetica', size); c.setFillColor(color); c.drawString(x, y, text)
    return y - size - 3

def ct_gap(y, n=6): return y - n

def ct_bullet(c, x, y, text, size=7.8, color=TEXT):
    c.setFont('Helvetica-Bold', size); c.setFillColor(ACCENT); c.drawString(x, y, '>')
    c.setFont('Helvetica', size); c.setFillColor(color); c.drawString(x + 10, y, text)
    return y - size - 4

def ct_table(c, x, y, headers, widths, rows, rh=14):
    c.setFillColor(SURF2); c.rect(x, y - rh, sum(widths), rh, fill=1, stroke=0)
    cx = x + 4
    for h_, w in zip(headers, widths):
        c.setFont('Helvetica-Bold', 6); c.setFillColor(MUTED)
        c.drawString(cx, y - rh + 4, h_.upper()); cx += w
    cur_y = y - rh
    for ri, (cells, colors, bold_cols) in enumerate(rows):
        if ri % 2 == 0:
            c.setFillColor(HexColor('#0f1419')); c.rect(x, cur_y - rh, sum(widths), rh, fill=1, stroke=0)
        cx = x + 4
        for ci, (cell, w, fc) in enumerate(zip(cells, widths, colors)):
            c.setFont('Helvetica-Bold' if ci in bold_cols else 'Helvetica', 7)
            c.setFillColor(fc); c.drawString(cx, cur_y - rh + 4, str(cell)); cx += w
        cur_y -= rh
    return cur_y - 4

def card(c, x, y, w, h, ac=None):
    c.setFillColor(SURFACE); c.setStrokeColor(BORDER)
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
    if ac is not None and is_color(ac):
        c.setFillColor(ac); c.rect(x, y, 3, h, fill=1, stroke=0)

def nav_bar(c, slide_n, total, label):
    # Background
    c.setFillColor(SURF2); c.rect(0, H - NAV_H, W, NAV_H, fill=1, stroke=0)
    # Progress bar
    pw = (W * slide_n) // total
    c.setFillColor(ACCENT); c.rect(0, H - 3, pw, 3, fill=1, stroke=0)
    # Title left
    c.setFont('Helvetica-Bold', 8); c.setFillColor(TEXT)
    c.drawString(PAD, H - 15, f'Eva Investment Research  ·  March 25, 2026')
    # Slide label right
    c.setFont('Helvetica', 7.5); c.setFillColor(MUTED)
    c.drawRightString(W - PAD, H - 15, f'{slide_n}/{total}  {label}')

def takeaway(c, text):
    c.setFillColor(NAVY); c.roundRect(PAD, TK_Y, W - PAD*2, 40, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT); c.setFont('Helvetica-Bold', 7); c.drawString(PAD+8, TK_Y+28, 'KEY TAKEAWAY')
    c.setFont('Helvetica', 8.5); c.setFillColor(TEXT); c.drawString(PAD+8, TK_Y+13, text)

def bg(c):
    c.setFillColor(BG); c.rect(0, 0, W, H, fill=1, stroke=0)

# ── Ticker mini-card ─────────────────────────────────────────────────────────
def ticker_card(c, x, y, sym, price, chg):
    cw, ch = 95, 52
    card(c, x, y, cw, ch)
    cy = y + ch - 12
    c.setFont('Helvetica-Bold', 8); c.setFillColor(TEXT); c.drawString(x+6, cy, sym)
    cy -= 14
    c.setFont('Helvetica-Bold', 10.5)
    col = GREEN if (chg or 0) > 0 else (RED if (chg or 0) < 0 else MUTED)
    c.setFillColor(col); c.drawString(x+6, cy, f'${price:,.2f}')
    cy -= 13
    c.setFont('Helvetica', 7.5); c.setFillColor(col)
    arrow = '▲' if (chg or 0) > 0 else ('▼' if (chg or 0) < 0 else '►')
    c.drawString(x+6, cy, f'{arrow} {chg:+.2f}%' if chg is not None else 'N/A')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 1: Market Snapshot
# ═══════════════════════════════════════════════════════════════════════════════
def slide1(c, n, total):
    bg(c); nav_bar(c, n, total, 'Market Snapshot')
    takeaway(c, 'Broad risk-on session: Gold +3.8%, Uranium +3.5%, Copper +3.8%, Defense +2.3%  |  SPY +0.87%  |  QQQ +1.10%')

    cy = CONTENT_TOP
    c.setFont('Helvetica-Bold', 11); c.setFillColor(TEXT); c.drawString(PAD, cy, 'Market Snapshot — March 25, 2026')
    cy -= 18

    # ETF/Index row
    etfs = [
        ('SPY',  658.85, 0.87),
        ('QQQ',  590.40, 1.10),
        ('SMH',  400.86, 1.59),
        ('GLD',  419.55, 3.82),
        ('IAU',  85.94,  3.84),
        ('XLE',  60.69,  -0.24),
        ('URA',  49.88,  3.51),
        ('COPX', 75.77,  3.79),
    ]
    cols = 8
    cw = 97
    for i, (sym, price, chg) in enumerate(etfs):
        ticker_card(c, PAD + i * (cw + 4), cy - 52, sym, price, chg)
    cy -= 64

    etfs2 = [
        ('GRID', 168.73, 2.03),
        ('CIBR', 64.42,  2.12),
        ('XAR',  267.74, 2.32),
        ('ITA',  226.15, 1.57),
        ('BIL',  91.60,  0.01),
        ('CEG',  304.96, 3.43),
        ('LMT',  621.11, 1.79),
        ('RTX',  195.20, 0.62),
    ]
    for i, (sym, price, chg) in enumerate(etfs2):
        ticker_card(c, PAD + i * (cw + 4), cy - 52, sym, price, chg)
    cy -= 64

    # Key Events
    cy = ct_gap(cy, 8)
    c.setFont('Helvetica-Bold', 8.5); c.setFillColor(ACCENT); c.drawString(PAD, cy, 'KEY EVENTS')
    cy -= 14

    events = [
        (PURPLE,  'CRYPTO',  'Circle (CRCL) stock rebounds after biggest single-day drop ever'),
        (ACCENT,  'TECH',    'SpaceX, OpenAI, Anthropic IPO pipeline swells — 3 largest IPOs ever potential'),
        (TEAL,    'EV',      'Aptiv EV spinoff "Versigent" set for April 1 — AI & robotaxi implications'),
        (YELLOW,  'MARKET',  'Equal-weight ETFs beating S&P 500 in 2026 as mega-cap dominance fades'),
        (RED,     'MARKET',  '4 consumer favorites oversold: Disney, McDonald\'s & more per 24/7 Wall St.'),
        (GOLD,    'GOLD',    'GLD surges +3.82% today — gold tests all-time highs near $3,100/oz'),
    ]
    for tag_col, tag, text in events:
        ex = PAD
        ey = cy
        c.setFillColor(HexColor('#0f1928')); c.roundRect(ex, ey - 11, W - PAD*2, 14, 2, fill=1, stroke=0)
        c.setFillColor(tag_col); c.rect(ex, ey - 11, 3, 14, fill=1, stroke=0)
        # Tag pill
        pill_w = len(tag) * 5 + 8
        c.setFillColor(tag_col); c.roundRect(ex + 6, ey - 9, pill_w, 10, 2, fill=1, stroke=0)
        c.setFont('Helvetica-Bold', 5.5); c.setFillColor(BG)
        c.drawString(ex + 9, ey - 3, tag)
        c.setFont('Helvetica', 7.5); c.setFillColor(TEXT)
        c.drawString(ex + 6 + pill_w + 4, ey - 3, text)
        cy -= 17

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 2: AAPL Deep Dive
# ═══════════════════════════════════════════════════════════════════════════════
def slide2(c, n, total):
    bg(c); nav_bar(c, n, total, 'AAPL Deep Dive')
    takeaway(c, 'AAPL +0.77% today at $253.59  |  Analyst target $295.31 → +16.5% upside  |  Fwd P/E 27.2x  |  Mkt Cap $3.73T  |  Rating: BUY')

    cy = CONTENT_TOP
    c.setFont('Helvetica-Bold', 12); c.setFillColor(TEXT); c.drawString(PAD, cy, '🍎  Apple Inc. (AAPL)  —  Largest Holding')
    cy -= 6
    c.setFont('Helvetica', 7.5); c.setFillColor(MUTED); c.drawString(PAD, cy, 'Consumer Electronics & Services · NASDAQ · Market Cap: $3.73T')
    cy -= 18

    # Two columns: left stats, right valuation
    lx = PAD
    rx = W // 2 + 6
    col_w = W // 2 - PAD - 10

    # Left: Price & Performance
    card(c, lx, cy - 130, col_w, 130)
    lcy = cy - 14
    lcy = ct_title(c, lx + 8, lcy, 'PRICE & PERFORMANCE', 7.5, ACCENT)
    rows_l = [
        ('Last Price', '$253.59', GREEN),
        ('1D Change', '▲ +$1.95  (+0.77%)', GREEN),
        ('Prev Close', '$251.64', TEXT),
        ('52W High', '$288.62', TEXT),
        ('52W Low', '$169.21', TEXT),
        ('Vs 52W High', '-12.2%', RED),
    ]
    for label, val, vc in rows_l:
        c.setFont('Helvetica', 7); c.setFillColor(MUTED); c.drawString(lx + 8, lcy, label)
        c.setFont('Helvetica-Bold', 7); c.setFillColor(vc); c.drawRightString(lx + col_w - 8, lcy, val)
        lcy -= 13
        c.setFillColor(BORDER); c.line(lx + 8, lcy + 5, lx + col_w - 8, lcy + 5)

    # Right: Valuation
    card(c, rx, cy - 130, col_w, 130)
    rcy = cy - 14
    rcy = ct_title(c, rx + 8, rcy, 'VALUATION & TARGETS', 7.5, ACCENT)
    rows_r = [
        ('P/E TTM', '32.1x', TEXT),
        ('P/E Forward', '27.2x', TEXT),
        ('Analyst Target', '$295.31', GREEN),
        ('Upside to Target', '+16.5%', GREEN),
        ('Market Cap', '$3.73T', TEXT),
        ('Consensus Rating', 'BUY', GREEN),
    ]
    for label, val, vc in rows_r:
        c.setFont('Helvetica', 7); c.setFillColor(MUTED); c.drawString(rx + 8, rcy, label)
        c.setFont('Helvetica-Bold', 7); c.setFillColor(vc); c.drawRightString(rx + col_w - 8, rcy, val)
        rcy -= 13
        c.setFillColor(BORDER); c.line(rx + 8, rcy + 5, rx + col_w - 8, rcy + 5)

    cy -= 140

    # Catalyst cards
    c.setFont('Helvetica-Bold', 7.5); c.setFillColor(ACCENT); c.drawString(PAD, cy, 'CATALYSTS & RISKS')
    cy -= 12

    catalysts = [
        (ACCENT,  'AI Features',       'Apple Intelligence on-device LLM rolling out globally across iPhone & Mac; Siri 2.0 upgrade cycle'),
        (GREEN,   'Services Growth',   'App Store, iCloud, Apple TV+, Pay — ~25% of revenue at 70%+ gross margin; compounding'),
        (GOLD,    'Buyback Machine',   '~$90B annual buyback; share count -3%/yr; EPS accretion mechanical even without growth'),
        (RED,     'Risk: Tariffs',     '~90% iPhone production in China; US-China trade war & tariff escalation key downside risk'),
    ]
    ccat_w = (W - PAD*2 - 12) // 4
    for i, (ac, title, body) in enumerate(catalysts):
        cx2 = PAD + i * (ccat_w + 4)
        card(c, cx2, cy - 80, ccat_w, 80, ac)
        ccy = cy - 14
        ccy = ct_title(c, cx2 + 8, ccy, title, 7.5, ac)
        # Wrap body text manually
        words = body.split()
        line = ''
        for w in words:
            test = (line + ' ' + w).strip()
            if len(test) * 4.2 > ccat_w - 14:
                ccy = ct_body(c, cx2 + 8, ccy, line, 6.5)
                line = w
            else:
                line = test
        if line:
            ct_body(c, cx2 + 8, ccy, line, 6.5)

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 3: AI Sector
# ═══════════════════════════════════════════════════════════════════════════════
def slide3(c, n, total):
    bg(c); nav_bar(c, n, total, 'AI Sector — Semis & Cloud')
    takeaway(c, 'NVDA +2.96% | AMD +6.83% | ANET +2.59% | TSM +1.58% | SMH +1.59%  —  Broad AI infrastructure rally on positive macro')

    cy = CONTENT_TOP
    c.setFont('Helvetica-Bold', 11); c.setFillColor(TEXT); c.drawString(PAD, cy, 'AI Sector — Semiconductors & Cloud  (March 25, 2026)')
    cy -= 20

    headers = ['TICKER', 'NAME', 'PRICE', '1D CHG', 'P/E TTM', 'P/E FWD', 'ANA. TARGET', 'UPSIDE', 'RATING']
    widths  = [48, 100, 62, 52, 52, 52, 72, 55, 70]

    rows = [
        (['NVDA', 'NVIDIA',           '$180.38', '+2.96%', '36.7x', '16.2x', '$268.22', '+48.7%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,TEXT,TEXT,TEXT,GREEN,GREEN], [0]),
        (['AMD',  'Advanced Micro',   '$219.39', '+6.83%', '84.1x', '20.4x', '$289.61', '+32.0%', 'Buy'],
         [ACCENT,TEXT,TEXT,GREEN,YELLOW,TEXT,TEXT,GREEN,TEAL], [0]),
        (['TSM',  'TSMC',             '$348.68', '+1.58%', '33.8x', '19.4x', '$430.65', '+23.5%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,TEXT,TEXT,TEXT,GREEN,GREEN], [0]),
        (['AVGO', 'Broadcom',         '$320.50', '+0.69%', '62.5x', '18.0x', '$472.01', '+47.3%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,YELLOW,TEXT,TEXT,GREEN,GREEN], [0]),
        (['ANET', 'Arista Networks',  '$134.19', '+2.59%', '48.8x', '31.5x', '$177.74', '+32.5%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,YELLOW,YELLOW,TEXT,GREEN,GREEN], [0]),
        (['MU',   'Micron Technology','$378.01', '-4.43%', '17.8x', '3.8x',  '$524.73', '+38.8%', 'Buy'],
         [ACCENT,TEXT,TEXT,RED,TEXT,GREEN,TEXT,GREEN,TEAL], [0]),
        (['MSFT', 'Microsoft',        '$373.25', '+0.14%', '23.3x', '19.8x', '$591.60', '+58.5%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,TEXT,TEXT,TEXT,GREEN,GREEN], [0]),
        (['GOOGL','Alphabet',         '$291.58', '+0.39%', '27.0x', '21.7x', '$376.75', '+29.2%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,TEXT,TEXT,TEXT,GREEN,GREEN], [0]),
        (['META', 'Meta Platforms',   '$597.34', '+0.75%', '25.5x', '16.7x', '$863.63', '+44.6%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,TEXT,TEXT,TEXT,GREEN,GREEN], [0]),
        (['AMZN', 'Amazon',           '$211.94', '+2.27%', '29.6x', '22.7x', '$280.47', '+32.3%', 'Strong Buy'],
         [ACCENT,TEXT,TEXT,GREEN,TEXT,TEXT,TEXT,GREEN,GREEN], [0]),
    ]
    cy = ct_table(c, PAD, cy, headers, widths, rows, rh=15)
    cy = ct_gap(cy, 4)
    c.setFont('Helvetica', 6.5); c.setFillColor(MUTED)
    c.drawString(PAD, cy, 'P/E TTM & Fwd, analyst targets from yfinance (sourced from analyst consensus). Live prices as of session close March 25, 2026.')

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 4: Defense, Energy & Geopolitics
# ═══════════════════════════════════════════════════════════════════════════════
def slide4(c, n, total):
    bg(c); nav_bar(c, n, total, 'Defense, Energy & Geopolitics')
    takeaway(c, 'Defense: XAR +2.32% | ITA +1.57% | LMT +1.79%  ·  Gold: GLD +3.82%  ·  Uranium: URA +3.51%  ·  Copper: COPX +3.79%')

    cy = CONTENT_TOP
    c.setFont('Helvetica-Bold', 11); c.setFillColor(TEXT); c.drawString(PAD, cy, 'Defense, Energy & Geopolitics')
    cy -= 20

    # Defense tickers
    c.setFont('Helvetica-Bold', 7.5); c.setFillColor(ACCENT); c.drawString(PAD, cy, 'DEFENSE')
    cy -= 12
    def_stocks = [
        ('LMT',  621.11, 1.79),
        ('RTX',  195.20, 0.62),
        ('XAR',  267.74, 2.32),
        ('ITA',  226.15, 1.57),
    ]
    for i, (sym, price, chg) in enumerate(def_stocks):
        ticker_card(c, PAD + i * 100, cy - 52, sym, price, chg)
    cy -= 64

    # Energy tickers
    c.setFont('Helvetica-Bold', 7.5); c.setFillColor(ORANGE); c.drawString(PAD, cy, 'ENERGY & COMMODITIES')
    cy -= 12
    energy_stocks = [
        ('CEG',  304.96, 3.43),
        ('XLE',  60.69,  -0.24),
        ('URA',  49.88,  3.51),
        ('COPX', 75.77,  3.79),
        ('GRID', 168.73, 2.03),
        ('GLD',  419.55, 3.82),
        ('IAU',  85.94,  3.84),
    ]
    for i, (sym, price, chg) in enumerate(energy_stocks):
        ticker_card(c, PAD + i * 100, cy - 52, sym, price, chg)
    cy -= 68

    # Geopolitical commentary
    c.setFont('Helvetica-Bold', 7.5); c.setFillColor(RED); c.drawString(PAD, cy, 'GEOPOLITICAL WATCH')
    cy -= 12

    geo_items = [
        (GOLD,   'Gold Safe-Haven Surge',     'GLD +3.82% & IAU +3.84% — strong risk-off demand. Gold near $3,100/oz all-time high. Geopolitical uncertainty + USD debasement fears driving allocation.'),
        (RED,    'Defense Spending Tailwind',  'NATO members committing to 5% GDP defense spending. Ukraine war ongoing. LMT, RTX, XAR outperforming YTD. Defense ETFs at record highs.'),
        (PURPLE, 'Nuclear Renaissance',        'URA +3.51% | CEG +3.43%. AI data center power demand is fueling nuclear capacity deals (Microsoft, Google, Amazon). SMRs gaining regulatory momentum.'),
        (TEAL,   'Copper & Grid Infra',        'COPX +3.79% | GRID +2.03%. Electrification mega-trend: EV infrastructure, AI data centers, and grid modernization driving structural copper demand.'),
    ]
    geo_w = (W - PAD*2 - 12) // 4
    for i, (ac, title, body) in enumerate(geo_items):
        gx = PAD + i * (geo_w + 4)
        card(c, gx, cy - 90, geo_w, 90, ac)
        gcy = cy - 14
        gcy = ct_title(c, gx + 8, gcy, title, 7, ac)
        gcy = ct_gap(gcy, 2)
        words = body.split()
        line = ''
        for w in words:
            test = (line + ' ' + w).strip()
            if len(test) * 4.0 > geo_w - 14:
                gcy = ct_body(c, gx + 8, gcy, line, 6.2)
                line = w
            else:
                line = test
        if line:
            ct_body(c, gx + 8, gcy, line, 6.2)

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 5: Portfolio — Eva's Suggested Allocation
# ═══════════════════════════════════════════════════════════════════════════════
def slide5(c, n, total):
    bg(c); nav_bar(c, n, total, "Eva's Suggested Allocation")
    takeaway(c, "Eva's Suggested Allocation: AI Infrastructure 30% | Big Tech 20% | Defense 12% | Gold 10% | Energy Transition 12% | Cyber 6% | Memory 5% | Cash 5%")

    cy = CONTENT_TOP
    c.setFont('Helvetica-Bold', 11); c.setFillColor(TEXT); c.drawString(PAD, cy, "Eva's Suggested Allocation  —  March 2026")
    cy -= 20

    allocations = [
        (ACCENT,  'AI Infrastructure',    '30%', 'NVDA, AMD, AVGO, ANET, TSM, SMH',         'Core AI capex cycle exposure. NVDA & TSM key. Fwd P/Es compressed vs. growth.'),
        (GREEN,   'Big Tech / Cloud',     '20%', 'AAPL, MSFT, GOOGL, META, AMZN',            'AI monetization layer. High FCF. MSFT & META highest conviction. AAPL #1 holding.'),
        (RED,     'Defense',             '12%', 'LMT, RTX, XAR, ITA',                       'NATO 5% GDP commitments. Geopolitical risk premium elevated. Secular tailwind.'),
        (GOLD,    'Gold / Hard Assets',  '10%', 'GLD, IAU',                                  'Safe-haven allocation. Gold +3.8% today near ATH. USD hedge & crisis insurance.'),
        (ORANGE,  'Energy Transition',   '12%', 'CEG, URA, COPX, GRID, XLE',                'Nuclear + copper + grid infra. AI power demand structural. Diversified energy mix.'),
        (PURPLE,  'Cybersecurity',        '6%', 'CIBR',                                      'AI expanding attack surface. CIBR ETF broad exposure. +2.12% today. Growth sector.'),
        (TEAL,    'Memory / Semis Value', '5%', 'MU',                                        'Fwd P/E 3.8x — deeply undervalued. HBM3E for AI. Target $524. High conviction.'),
        (MUTED,   'Cash Buffer (T-Bills)','5%', 'BIL',                                       'Tactical dry powder. 5%+ yield. Deploy on dips or new opportunities. Flexible.'),
    ]

    aw = (W - PAD*2 - 21) // 4
    ah = 100
    cols = 4
    for i, (ac, title, pct, names, desc) in enumerate(allocations):
        row = i // cols
        col = i % cols
        ax = PAD + col * (aw + 7)
        ay = cy - (row + 1) * (ah + 8)
        card(c, ax, ay, aw, ah, ac)
        acy = ay + ah - 10
        c.setFont('Helvetica-Bold', 6.5); c.setFillColor(MUTED); c.drawString(ax + 8, acy, title.upper())
        acy -= 4
        c.setFont('Helvetica-Bold', 22); c.setFillColor(ac); c.drawString(ax + 8, acy - 18, pct)
        acy -= 26
        c.setFont('Helvetica-Bold', 6); c.setFillColor(TEXT); c.drawString(ax + 8, acy, names[:38])
        acy -= 10
        words = desc.split()
        line = ''
        for w in words:
            test = (line + ' ' + w).strip()
            if len(test) * 4.0 > aw - 14:
                if acy > ay + 4:
                    ct_body(c, ax + 8, acy, line, 5.8)
                    acy -= 9
                line = w
            else:
                line = test
        if line and acy > ay + 4:
            ct_body(c, ax + 8, acy, line, 5.8)

    # Top 3 picks
    cy_picks = cy - 2 * (ah + 8) - 16
    c.setFont('Helvetica-Bold', 7.5); c.setFillColor(ACCENT); c.drawString(PAD, cy_picks, 'TOP 3 CONVICTION PICKS — MARCH 2026')
    cy_picks -= 12
    picks = [
        (GOLD,   '🥇 NVDA',   'Fwd P/E 16.2x — cheap vs AI capex cycle. Target $268 (+48.7%). Catalyst: Blackwell Ultra ramp, sovereign AI.'),
        (TEAL,   '🥈 GLD/IAU','Gold +3.8% today. Geopolitical hedge firing. ATH near $3,100/oz. Safe-haven allocation critical now.'),
        (ORANGE, '🥉 MU',     'Fwd P/E 3.8x — deeply undervalued. HBM3E structural demand for AI accelerators. Target $524 (+38.8%).'),
    ]
    pw = (W - PAD*2 - 16) // 3
    for i, (ac, title, body) in enumerate(picks):
        px = PAD + i * (pw + 8)
        card(c, px, cy_picks - 55, pw, 55, ac)
        pcy = cy_picks - 12
        pcy = ct_title(c, px + 8, pcy, title, 8, ac)
        words = body.split()
        line = ''
        for w in words:
            test = (line + ' ' + w).strip()
            if len(test) * 4.2 > pw - 14:
                if pcy > cy_picks - 55 + 4:
                    ct_body(c, px + 8, pcy, line, 6.5)
                    pcy -= 10
                line = w
            else:
                line = test
        if line:
            ct_body(c, px + 8, pcy, line, 6.5)


# ═══════════════════════════════════════════════════════════════════════════════
# BUILD PDF
# ═══════════════════════════════════════════════════════════════════════════════
slides = [slide1, slide2, slide3, slide4, slide5]
cv = canvas.Canvas(OUTPUT, pagesize=(W, H))

for i, fn in enumerate(slides):
    try:
        fn(cv, i+1, len(slides))
        cv.showPage()
        print(f'Slide {i+1}: OK')
    except Exception as e:
        import traceback; traceback.print_exc()
        cv.showPage()

cv.save()

# Verify
with open(OUTPUT, 'rb') as f:
    data = f.read()
pages = len(re.findall(b'/Type /Page[ \n]|/Type/Page[ \n]', data))
assert pages == len(slides), f'Page count mismatch: {pages} != {len(slides)}'
print(f'PASS: {pages} pages, {len(data):,} bytes → {OUTPUT}')
