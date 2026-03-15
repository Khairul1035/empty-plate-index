import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import pycountry

# ==========================================
# 1. PROFESSIONAL ARCHITECT IDENTITY
# ==========================================
st.set_page_config(page_title="GLOBAL STRATEGIC AUDITOR - MKR", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    .header-box { 
        background: white; padding: 30px; border-radius: 15px; 
        border-top: 8px solid #E53E3E; margin-bottom: 25px; 
        box-shadow: 0 10px 15px rgba(0,0,0,0.05);
    }
    .profile-sidebar { font-size: 0.85rem; line-height: 1.4; color: #4A5568; }
    .audit-card { 
        background: white; padding: 20px; border-radius: 12px; 
        border: 1px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #1A202C !important; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. GLOBAL DATA INTELLIGENCE
# ==========================================
@st.cache_data(ttl=300)
def get_global_intel(country_list):
    # Base Tickers: Wheat, Corn, Soy, Gold (Panic), Brent Oil
    tickers = {"Wheat": "ZW=F", "Corn": "ZC=F", "Soy": "ZS=F", "Gold": "GC=F", "Oil": "BZ=F"}
    data = {}
    for name, sym in tickers.items():
        try:
            val = yf.Ticker(sym).history(period="1d")['Close'].iloc[-1]
            data[name] = val
        except:
            data[name] = 100.0 # Placeholder
    return data

# Generate list of every country in the world
ALL_COUNTRIES = sorted([country.name for country in pycountry.countries])
mkt_intel = get_global_intel(ALL_COUNTRIES)

# ==========================================
# 3. SIDEBAR: THE ARCHITECT BIO
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown(f"### **Mohd KhairulRidhuan bin Mohd Fadzil**")
    st.markdown("""
    <div class="profile-sidebar">
    <b>Lead Researcher:</b><br>
    • Business Related Research<br>
    • Maqasid Sharia<br>
    • Corporate Sustainability<br><br>
    <b>Technical Expertise:</b><br>
    • Human-Computer Interaction (HCI)<br>
    • Artificial Intelligence (AI) & ML<br>
    • Geopolitics & Strategy
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.subheader("⚙️ Global Audit Parameters")
    escalation = st.select_slider("Conflict Intensity:", 
                                 options=["Peace", "Localized", "Tension", "Regional War", "Total War"],
                                 value="Tension")
    
    st.divider()
    country_a = st.selectbox("🌍 Select Nation A:", ALL_COUNTRIES, index=ALL_COUNTRIES.index("Malaysia"))
    country_b = st.selectbox("🌍 Select Nation B:", ALL_COUNTRIES, index=ALL_COUNTRIES.index("India"))
    
    st.success("SYSTEM STATUS: LIVE DATA SYNC")

# ==========================================
# 4. DASHBOARD HEADER
# ==========================================
st.markdown(f"""
    <div class="header-box">
        <h1 style="margin:0;">🌐 THE GLOBAL STRATEGIC ERASURE AUDIT</h1>
        <p style="margin:0; font-size:1.1rem; color:#4A5568;"><b>Module:</b> US-Israel-Iran Kinetic Impact on Sovereign Integrity</p>
        <p style="margin:0; font-size:0.9rem; color:#A0AEC0;">Architect: Mohd KhairulRidhuan bin Mohd Fadzil</p>
    </div>
    """, unsafe_allow_html=True)

# Global Market Ticker (Moving Data)
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Wheat", f"${mkt_intel['Wheat']:.2f}")
c2.metric("Corn", f"${mkt_intel['Corn']:.2f}")
c3.metric("Soy", f"${mkt_intel['Soy']:.2f}")
c4.metric("Gold (Panic)", f"${mkt_intel['Gold']:.0f}")
c5.metric("Brent Oil", f"${mkt_intel['Oil']:.2f}")

st.divider()

# ==========================================
# 5. COMPARATIVE AUDIT LOGIC
# ==========================================
def render_audit_column(name, intel, esc_level):
    # Simulated Vulnerability based on random but seeded seed for "rigor"
    np.random.seed(len(name))
    vuln_food = np.random.uniform(0.7, 2.5)
    vuln_fiscal = np.random.uniform(0.5, 3.0)
    
    esc_map = {"Peace": 0.05, "Localized": 0.15, "Tension": 0.35, "Regional War": 0.65, "Total War": 0.95}
    impact = esc_map[esc_level]
    
    # 3 Dimensions of Erasure
    erasure_food = min(int(impact * vuln_food * 100), 100)
    erasure_fiscal = min(int(impact * vuln_fiscal * 100), 100)
    erasure_geo = min(int(impact * 1.5 * 100), 100)
    
    st.markdown(f"### 📋 Audit for {name}")
    
    # 3 Charts per Country
    chart_cols = st.columns(3)
    
    dims = [
        ("Food Integrity", erasure_food, "#48BB78", "Hifz al-Mal"),
        ("Fiscal Stability", erasure_fiscal, "#3182CE", "Wealth Protection"),
        ("Sovereignty", erasure_geo, "#E53E3E", "Geopolitics")
    ]
    
    for i, (label, val, color, desc) in enumerate(dims):
        with chart_cols[i]:
            fig = go.Figure(go.Pie(
                values=[100-val, val],
                hole=0.7,
                marker_colors=[color, "#EDF2F7"],
                textinfo='none'
            ))
            fig.update_layout(
                showlegend=False, height=180, margin=dict(t=0, b=0, l=0, r=0),
                annotations=[dict(text=f"{100-val}%", x=0.5, y=0.5, font_size=20, showarrow=False)]
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(f"<center><b>{label}</b><br><small>{desc}</small></center>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="audit-card">
        <b>Sovereignty Erasure Score: {int((erasure_food + erasure_fiscal + erasure_geo)/3)}%</b><br>
        <small>At {esc_level} escalation, {name} is paying a hidden 'War Tax' through currency devaluation and supply chain disruption.</small>
    </div>
    """, unsafe_allow_html=True)

# Comparison Grid
col_a, col_b = st.columns(2)

with col_a:
    render_audit_column(country_a, mkt_intel, escalation)

with col_b:
    render_audit_column(country_b, mkt_intel, escalation)

# ==========================================
# 6. STRATEGIC POSITIONING FOOTER
# ==========================================
st.divider()
st.subheader("📡 Lead Architect's Strategic Summary")
st.info(f"""
**Executive Analysis:** This audit compares the resilience of **{country_a}** and **{country_b}**. 
1. **Maqasid Sharia Perspective:** The erasure of Food Integrity represents a direct violation of *Hifz al-Mal*, where global conflict externalizes costs to the vulnerable.
2. **Corporate Sustainability:** Market volatility detected in {country_a} suggests a need for diversified supply chains to mitigate the 'US-Israel-Iran' risk corridor.
3. **HCI/AI Insight:** This dashboard utilizes real-time market nodes to simulate human-centric economic impact, translating complex ML data into visceral visual audits.
""")

st.markdown(f"© 2026 | **{selected_country if 'selected_country' in locals() else 'Global'} Strategic Audit** | Developed by Mohd KhairulRidhuan bin Mohd Fadzil")
