import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# ==========================================
# 1. STRATEGIC BRANDING & UI
# ==========================================
st.set_page_config(page_title="GLOBAL SOVEREIGNTY AUDITOR", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    .brand-box { background: white; padding: 20px; border-radius: 10px; border-bottom: 5px solid #E53E3E; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .audit-card { background: white; padding: 25px; border-radius: 15px; border-left: 10px solid #E53E3E; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    h1, h2, h3, p, span { color: #1A202C !important; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. DATA ENGINE (MULTI-CURRENCY & COMMODITY)
# ==========================================
@st.cache_data(ttl=60)
def get_strategic_data(country_name):
    # Mapping Country to Currency Tickers
    currency_map = {
        "Malaysia": "USDMYR=X", "United Kingdom": "GBP=X", "Japan": "JPY=X", 
        "Germany": "EUR=X", "Egypt": "USDEGP=X", "India": "INR=X", "Singapore": "USDSGD=X"
    }
    cur_ticker = currency_map.get(country_name, "USD=X")
    
    # Fetch Data: Wheat, Corn, and Currency Exchange Rate
    tickers = {"Wheat": "ZW=F", "Corn": "ZC=F", "Rate": cur_ticker}
    prices = {}
    for name, sym in tickers.items():
        try:
            val = yf.Ticker(sym).history(period="1d")['Close'].iloc[-1]
            prices[name] = val
        except:
            prices[name] = 650.0 if name == "Wheat" else 1.0 # Fallback
    return prices

# ==========================================
# 3. SIDEBAR & BRANDING
# ==========================================
with st.sidebar:
    st.markdown("### 👤 PROJECT ARCHITECT")
    st.info("**Mohd Khairul Ridhuan**\n\n*Worldwide Strategic Intelligence*")
    st.divider()
    
    # INTERACTIVE TRIGGER 1: Country Selection
    country = st.selectbox("🌍 SELECT NATION TO AUDIT:", 
                          ["Malaysia", "United Kingdom", "Egypt", "Singapore", "India", "Germany"])
    
    # INTERACTIVE TRIGGER 2: Escalation
    escalation = st.select_slider("🔥 WAR ESCALATION LEVEL:", 
                                 options=["Peace", "Localized", "High Tension", "Regional War", "Total War"],
                                 value="High Tension")
    st.divider()
    st.success(f"AUDITING: {country.upper()}")

# Load Data based on selected country
mkt = get_strategic_data(country)
exchange_rate = mkt['Rate'] if country != "USA" else 1.0
cur_symbol = {"Malaysia": "RM", "United Kingdom": "£", "Egypt": "E£", "Germany": "€", "Singapore": "S$"}.get(country, "$")

# ==========================================
# 4. MAIN DASHBOARD
# ==========================================
st.markdown(f"""
    <div class="brand-box">
        <h1 style="margin:0;">🍽️ THE EMPTY PLATE INDEX: {country.upper()}</h1>
        <p style="margin:0;">Real-Time Sovereignty Loss Audit | Developed by Mohd Khairul Ridhuan</p>
    </div>
    """, unsafe_allow_html=True)

# Market Pulse (Converted to Local Currency)
c1, c2, c3 = st.columns(3)
with c1: st.metric(f"Wheat Price ({cur_symbol})", f"{cur_symbol}{mkt['Wheat'] * exchange_rate / 100:.2f}", "Local Market Cost")
with c2: st.metric(f"Corn Price ({cur_symbol})", f"{cur_symbol}{mkt['Corn'] * exchange_rate / 100:.2f}", "Feed/Protein Cost")
with c3: st.metric("Exchange Rate", f"{exchange_rate:.2f}", f"vs USD")

st.divider()

# ==========================================
# 5. DYNAMIC IMPACT CALCULATION
# ==========================================
# Vulnerability Factor (Rich vs Poor nations)
vulnerability = {"Malaysia": 1.2, "Egypt": 2.5, "United Kingdom": 0.8, "Singapore": 0.7, "India": 1.8, "Germany": 0.9}.get(country, 1.0)
esc_impact = {"Peace": 0.05, "Localized": 0.15, "High Tension": 0.35, "Regional War": 0.65, "Total War": 0.90}[escalation]

# Total "Erasure" of the plate
erased_pct = int(esc_impact * vulnerability * 100)
erased_pct = min(erased_pct, 100) # Max 100%
remaining_pct = 100 - erased_pct

col_viz, col_audit = st.columns([1.5, 1])

with col_viz:
    # Responsive Chart
    fig = go.Figure(go.Pie(
        values=[remaining_pct, erased_pct],
        labels=['Sovereign Portion', 'War Erasure'],
        hole=.75,
        marker_colors=['#48BB78', '#F56565'],
        textinfo='none'
    ))
    fig.update_layout(
        title=f"National Food Integrity: {country}",
        annotations=[dict(text=f'{remaining_pct}%', x=0.5, y=0.5, font_size=50, showarrow=False)]
    )
    st.plotly_chart(fig, use_container_width=True)

with col_audit:
    st.markdown(f"""
    <div class="audit-card">
        <h2 style="color:#E53E3E;">AUDIT REPORT</h2>
        <p><b>Target:</b> {country}</p>
        <p><b>Currency:</b> {cur_symbol} (Live Feed)</p>
        <hr>
        <h3>War Tax: {erased_pct}%</h3>
        <p>This is the amount of food 'stolen' from a typical {country} household plate due to US/Iran conflict escalation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning(f"**Strategist Analysis:** {country} is currently {'highly vulnerable' if vulnerability > 1.5 else 'moderately impacted'} by global supply chain erasure.")

st.caption(f"Data source: Real-time FX & Commodities | Lead Strategist: Mohd Khairul Ridhuan")
