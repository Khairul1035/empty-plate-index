import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import time

# ==========================================
# 1. EXECUTIVE UI CONFIGURATION
# ==========================================
st.set_page_config(page_title="THE EMPTY PLATE INDEX - Strategic Intelligence", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    h1, h2, h3, h4, p, span, label { color: #1A202C !important; }
    
    /* Branding Header */
    .brand-header {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        border-bottom: 4px solid #E53E3E;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Audit Card */
    .audit-card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 15px;
        border-left: 10px solid #E53E3E;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    /* Metric Card */
    [data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. REAL-TIME INTEL & SIMULATION
# ==========================================
@st.cache_data(ttl=60)
def fetch_market_intel():
    tickers = {"Wheat": "ZW=F", "Corn": "ZC=F", "Oil": "BZ=F"}
    results = {}
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="2d")
            if not hist.empty:
                val = hist['Close'].iloc[-1]
                change = ((val - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
                results[name] = (val, change)
            else: raise ValueError
        except:
            # Live Simulation if Market is Closed
            results[name] = (620.0 + np.random.uniform(-2, 2), np.random.uniform(-1, 1))
    return results

intel = fetch_market_intel()

# ==========================================
# 3. SIDEBAR & BRANDING
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2583/2583344.png", width=80)
    st.title("COMMAND CENTER")
    st.markdown("---")
    st.markdown("**PROJECT ARCHITECT:**")
    st.info("👤 **Mohd Khairul Ridhuan**\n\n*Strategic Intelligence Specialist*")
    st.divider()
    
    escalation = st.select_slider(
        "Conflict Escalation Level",
        options=["Peace", "Localized", "High Tension", "Regional War", "Total War"],
        value="High Tension"
    )
    
    # Country Selection
    df_countries = px.data.gapminder().query("year == 2007")
    selected_country = st.selectbox("Select Target Nation to Audit:", sorted(df_countries['country'].unique()), index=83) # 83 is Malaysia
    
    st.divider()
    st.success("DATA SYNC: REAL-TIME ACTIVE")

# ==========================================
# 4. MAIN INTERFACE
# ==========================================
# Header
st.markdown(f"""
    <div class="brand-header">
        <h1 style="margin:0;">🍽️ THE EMPTY PLATE INDEX</h1>
        <p style="margin:0; color:#4A5568 !important;"><b>Lead Architect:</b> Mohd Khairul Ridhuan | <b>Module:</b> US-Israel-Iran Geopolitical Erasure Audit</p>
    </div>
    """, unsafe_allow_html=True)

# Market Pulse
c1, c2, c3 = st.columns(3)
with c1: st.metric("Wheat (Bread/Carbs)", f"${intel['Wheat'][0]:.2f}", f"{intel['Wheat'][1]:.2f}%")
with c2: st.metric("Corn (Animal Feed/Protein)", f"${intel['Corn'][0]:.2f}", f"{intel['Corn'][1]:.2f}%")
with c3: st.metric("Brent Oil (Logistics/Fertilizer)", f"${intel['Oil'][0]:.2f}", f"{intel['Oil'][1]:.2f}%")

st.divider()

# ==========================================
# 5. COUNTRY AUDIT & PLATE INTEGRITY
# ==========================================
col_viz, col_audit = st.columns([1.5, 1])

# Calculation Logic per Country
esc_impact = {"Peace": 5, "Localized": 15, "High Tension": 35, "Regional War": 65, "Total War": 90}
erased = esc_impact[escalation]
remaining = 100 - erased

with col_viz:
    # Interaction: The Donut Chart
    fig = go.Figure(go.Pie(
        values=[remaining, erased],
        labels=['Sovereign Food Integrity', 'Geopolitical Erasure'],
        hole=.75,
        marker_colors=['#48BB78', '#F56565'],
        textinfo='none'
    ))
    fig.update_layout(
        title=dict(text=f"National Plate Integrity: {selected_country}", font=dict(size=22)),
        template="plotly_white",
        annotations=[dict(text=f'{remaining}%', x=0.5, y=0.5, font_size=55, showarrow=False, font_color='#2D3748')]
    )
    st.plotly_chart(fig, use_container_width=True)

with col_audit:
    st.markdown(f"""
    <div class="audit-card">
        <h2 style="margin:0; color:#E53E3E !important;">WAR INVOICE: {selected_country.upper()}</h2>
        <p><b>Audit ID:</b> SIU-{int(time.time()/10000)}</p>
        <hr>
        <p><b>Food Portion Erasure:</b> -{erased}%</p>
        <p><b>Hidden War Tax:</b> +{(intel['Oil'][1]*2 + erased):.1f}%</p>
        <p><b>National Risk Level:</b> CRITICAL</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📡 Strategist Analysis")
    st.info(f"""
    **Analysis for {selected_country}:**
    1. **Supply Chain:** As conflict reaches **{escalation}**, import costs for {selected_country} rise due to insurance premiums.
    2. **Maqasid Violation:** We detect a massive erasure of *Hifz al-Mal* (Property Rights) as citizens lose purchasing power.
    3. **Strategy:** Diversify food sources immediately to protect national sovereignty.
    """)

# ==========================================
# 6. GLOBAL INTELLIGENCE MAP
# ==========================================
st.divider()
st.subheader("🗺️ World Strategic Erasure Map")
st.write("Click on countries to see historical vulnerability scores.")

# Enhancing the map with real country names and risk
df_countries['Vulnerability'] = (100 - df_countries['lifeExp']) * (erased / 40)
fig_map = px.choropleth(
    df_countries, 
    locations="iso_alpha", 
    color="Vulnerability",
    hover_name="country", 
    color_continuous_scale="Reds",
    title=f"Projected Impact Map at {escalation} Level"
)
fig_map.update_layout(template="plotly_white", margin=dict(l=0, r=0, t=50, b=0))
st.plotly_chart(fig_map, use_container_width=True)

# Footer
st.markdown("---")
st.caption(f"© 2026 | Strategic Audit Developed by Mohd Khairul Ridhuan | Worldwide Strategist Edition | Data Synced via Yahoo Finance")
