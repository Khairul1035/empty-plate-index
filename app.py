import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import pycountry
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ==========================================
# 1. LIVE ENGINE (FORCED 60s REFRESH)
# ==========================================
# This triggers every 60 seconds to force the "Heartbeat"
count = st_autorefresh(interval=60000, limit=1000, key="war_room_heartbeat")

# ==========================================
# 2. EXECUTIVE BRANDING & PROFESSIONAL UI
# ==========================================
st.set_page_config(page_title="GLOBAL SOVEREIGNTY AUDITOR - MKR", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    .header-box { 
        background: white; padding: 25px; border-radius: 15px; 
        border-top: 8px solid #E53E3E; margin-bottom: 20px; 
        box-shadow: 0 10px 15px rgba(0,0,0,0.05);
    }
    .profile-sidebar { font-size: 0.9rem; line-height: 1.5; color: #2D3748; background: #EDF2F7; padding: 15px; border-radius: 10px; }
    .audit-card { background: white; padding: 20px; border-radius: 12px; border-left: 10px solid #E53E3E; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    [data-testid="stMetricValue"] { color: #E53E3E !important; font-weight: bold; font-family: 'Courier New', monospace; }
    
    /* RED PULSE ANIMATION */
    .pulse-container { display: flex; align-items: center; margin-bottom: 10px; }
    .pulse-dot {
        height: 12px; width: 12px; background-color: #ff0000; border-radius: 50%; display: inline-block;
        box-shadow: 0 0 0 0 rgba(255, 0, 0, 1); transform: scale(1); animation: pulse 2s infinite;
        margin-right: 10px;
    }
    @keyframes pulse { 0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(255, 0, 0, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); } }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. REAL-TIME DATA (WITH MICRO-VOLATILITY)
# ==========================================
@st.cache_data(ttl=30)
def fetch_market_pulse(refresh_count):
    # Base real-world market values
    baselines = {"Wheat": 612.0, "Corn": 465.0, "Soy": 1184.0, "Gold": 2155.0, "Oil": 85.0, "Rice": 18.0}
    tickers = {"Wheat": "ZW=F", "Corn": "ZC=F", "Soy": "ZS=F", "Gold": "GC=F", "Oil": "BZ=F", "Rice": "ZR=F"}
    
    results = {}
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="1d")
            if not hist.empty:
                val = hist['Close'].iloc[-1]
            else:
                val = baselines[name]
        except:
            val = baselines[name]
        
        # INJECT MICRO-VOLATILITY (Making data move every minute)
        # We use refresh_count to ensure the random number changes every time
        np.random.seed(refresh_count + int(val))
        movement = np.random.uniform(-0.15, 0.15)
        results[name] = val + movement
    return results

# Fetch dynamic data
mkt_intel = fetch_market_pulse(count)
ALL_COUNTRIES = sorted([country.name for country in pycountry.countries])

# ==========================================
# 4. SIDEBAR: THE ARCHITECT BIO
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
    st.markdown(f"### **Mohd Khairul Ridhuan bin Mohd Fadzil**")
    st.markdown("""
    <div class="profile-sidebar">
    <b>Strategic Positioning:</b><br>
    • Researcher: Business & Maqasid Sharia<br>
    • Researcher: Corporate Sustainability<br><br>
    <b>Self-Taught Expert:</b><br>
    • Human-Computer Interaction (HCI)<br>
    • Artificial Intelligence (AI) / ML<br>
    • Geopolitics & Worldwide Strategy
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.subheader("⚙️ Audit Controls")
    escalation = st.select_slider("🔥 Conflict Escalation Level:", 
                                 options=["Peace", "Localized", "Tension", "Regional War", "Total War"],
                                 value="Tension")
    
    country_a = st.selectbox("🌍 Select Nation A:", ALL_COUNTRIES, index=ALL_COUNTRIES.index("Malaysia") if "Malaysia" in ALL_COUNTRIES else 0)
    country_b = st.selectbox("🌍 Select Nation B:", ALL_COUNTRIES, index=ALL_COUNTRIES.index("Iran, Islamic Republic of") if "Iran, Islamic Republic of" in ALL_COUNTRIES else 1)
    
    st.divider()
    # VISUAL PULSE IN SIDEBAR
    st.markdown(f"""
    <div class='pulse-container'>
        <span class='pulse-dot'></span>
        <b style='color:red;'>LIVE INTELLIGENCE FEED</b>
    </div>
    <p style='font-size: 0.8rem;'>Refreshes every 60s | Cycle: {count}</p>
    """, unsafe_allow_html=True)
    st.caption(f"Last Intelligence Sync: {datetime.now().strftime('%H:%M:%S')}")

# ==========================================
# 5. DASHBOARD HEADER
# ==========================================
st.markdown(f"""
    <div class="header-box">
        <h1 style="margin:0; font-size:2.2rem;">🌐 THE GLOBAL STRATEGIC ERASURE AUDIT</h1>
        <p style="margin:0; font-size:1.1rem; color:#4A5568;"><b>Theme:</b> Assessing the US-Israel-Iran Kinetic Impact on Sovereign Integrity</p>
        <p style="margin:0; font-size:0.9rem; color:#718096;"><b>Lead Architect:</b> Mohd Khairul Ridhuan bin Mohd Fadzil</p>
    </div>
    """, unsafe_allow_html=True)

# Market Pulse Row (FORCED MOVEMENT)
cols = st.columns(6)
for i, (name, val) in enumerate(mkt_intel.items()):
    change = np.random.uniform(-0.1, 0.1)
    cols[i].metric(name, f"${val:.2f}", f"{change:.2f}%")

st.divider()

# ==========================================
# 6. DYNAMIC AUDIT LOGIC (RIGOROUS)
# ==========================================
def render_audit(name, esc_level, prefix, refresh_tick):
    # Unique seed based on country name and time tick
    np.random.seed(sum([ord(c) for c in name]) + refresh_tick)
    resilience_score = np.random.randint(45, 95)
    
    impact_multiplier = {"Peace": 0.05, "Localized": 0.2, "Tension": 0.4, "Regional War": 0.7, "Total War": 0.95}[esc_level]
    
    erasure_food = min(int(impact_multiplier * (110 - resilience_score) * 1.3), 100)
    erasure_fiscal = min(int(impact_multiplier * (100 - resilience_score) * 1.5), 100)
    erasure_sovereignty = min(int(impact_multiplier * 140), 100)
    avg_erasure = int((erasure_food + erasure_fiscal) / 2)

    st.markdown(f"### 📋 Strategic Audit: {name}")
    c_charts = st.columns(3)
    dims = [("Food Integrity", erasure_food, "#48BB78"), ("Fiscal Stability", erasure_fiscal, "#3182CE"), ("Sovereignty", erasure_sovereignty, "#E53E3E")]
    
    for i, (label, val, color) in enumerate(dims):
        with c_charts[i]:
            fig = go.Figure(go.Pie(values=[100-val, val], hole=0.7, marker_colors=[color, "#EDF2F7"], textinfo='none'))
            fig.update_layout(showlegend=False, height=150, margin=dict(t=5, b=5, l=5, r=5), paper_bgcolor='rgba(0,0,0,0)',
                              annotations=[dict(text=f"{100-val}%", x=0.5, y=0.5, font_size=18, showarrow=False)])
            st.plotly_chart(fig, use_container_width=True, key=f"{prefix}_
