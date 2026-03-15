import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import pycountry

# ==========================================
# 1. PROFESSIONAL ARCHITECT IDENTITY (FINAL)
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
    .profile-sidebar { font-size: 0.88rem; line-height: 1.5; color: #2D3748; }
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
def get_global_intel():
    # Expanding to include Rice and Fertilizer Proxy (Gas)
    tickers = {
        "Wheat": "ZW=F", "Corn": "ZC=F", 
        "Soy": "ZS=F", "Gold": "GC=F", 
        "Oil": "BZ=F", "Rice": "ZR=F"
    }
    data = {}
    for name, sym in tickers.items():
        try:
            val = yf.Ticker(sym).history(period="1d")['Close'].iloc[-1]
            data[name] = val
        except:
            data[name] = 0.0 
    return data

ALL_COUNTRIES = sorted([country.name for country in pycountry.countries])
mkt_intel = get_global_intel()

# ==========================================
# 3. SIDEBAR: THE ARCHITECT BIO
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown(f"### **Mohd KhairulRidhuan bin Mohd Fadzil**")
    st.markdown("""
    <div class="profile-sidebar">
    <b>Strategic Positioning:</b><br>
    • Researcher: Business Related Research<br>
    • Researcher: Maqasid Sharia<br>
    • Researcher: Corporate Sustainability<br><br>
    <b>Self-Taught Expert:</b><br>
    • Human-Computer Interaction (HCI)<br>
    • Artificial Intelligence (AI)<br>
    • Machine Learning (ML)<br>
    • Geopolitics & Strategy
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.subheader("⚙️ Audit Parameters")
    escalation = st.select_slider("Conflict Intensity:", 
                                 options=["Peace", "Localized", "Tension", "Regional War", "Total War"],
                                 value="Tension")
    
    st.divider()
    country_a = st.selectbo
