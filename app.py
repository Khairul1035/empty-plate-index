import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# ==========================================
# 1. STRATEGIC UI SETUP
# ==========================================
st.set_page_config(page_title="THE EMPTY PLATE INDEX", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .plate-border {
        background-color: #F8F9FA;
        padding: 50px;
        border-radius: 50%;
        border: 12px solid #E9ECEF;
        width: 380px;
        height: 380px;
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: inset 0 4px 15px rgba(0,0,0,0.05);
    }
    .food-icon { font-size: 70px; margin: 15px; transition: all 0.5s ease; }
    h1, h2, h3 { color: #1A202C !important; text-align: center; }
    .stSlider label { font-size: 18px !important; font-weight: bold; color: #2D3748; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. REAL-TIME MARKET INTELLIGENCE
# ==========================================
@st.cache_data(ttl=3600)
def fetch_global_commodities():
    # ZW=F (Wheat/Bread), ZC=F (Corn/Poultry Feed)
    tickers = {"Wheat": "ZW=F", "Corn": "ZC=F"}
    prices = {}
    for name, sym in tickers.items():
        try:
            val = yf.Ticker(sym).history(period="1d")['Close'].iloc[-1]
            prices[name] = val
        except:
            prices[name] = 600.0 if name == "Wheat" else 450.0 # Fallback values
    return prices

mkt = fetch_global_commodities()
# Historical Baselines (Peace-time averages)
baseline_wheat = 550.0 
baseline_corn = 430.0

# ==========================================
# 3. SIDEBAR: WAR SIMULATION
# ==========================================
with st.sidebar:
    st.header("🌍 Strategic Parameters")
    st.write("Simulating US/Israel vs Iran escalation impact on global supply chains.")
    
    escalation = st.select_slider(
        "Conflict Intensity",
        options=["Diplomacy", "Trade War", "High Tension", "Blockade", "Total War"],
        value="High Tension"
    )
    
    st.divider()
    st.info("**Strategist Note:** Blockades in the Middle East disrupt 30% of global fertilizer exports, directly impacting crop yields.")

# Logic: Portion Erosion
multiplier = {"Diplomacy": 1.0, "Trade War": 1.25, "High Tension": 1.6, "Blockade": 2.2, "Total War": 4.0}[escalation]

wheat_portion = max(0.05, (baseline_wheat / mkt['Wheat']) / multiplier)
corn_portion = max(0.05, (baseline_corn / mkt['Corn']) / multiplier)

# ==========================================
# 4. MAIN DASHBOARD
# ==========================================
st.title("🍽️ THE EMPTY PLATE INDEX")
st.markdown("### *Measuring the Global Erasure of Food Security*")
st.write(f"Real-time audit of how the US-Iran conflict 'erases' the dinner plate of the global middle class.")

st.divider()

# Visual Representation
st.markdown(f"""
    <div class="plate-border">
        <div class="food-icon" style="opacity: {wheat_portion}; transform: scale({wheat_portion});" title="Wheat/Bread">🍞</div>
        <div class="food-icon" style="opacity: {corn_portion}; transform: scale({corn_portion});" title="Poultry/Meat">🍗</div>
        <p style="color: #A0AEC0; font-family: monospace;">SOVEREIGN PORTION</p>
    </div>
    """, unsafe_allow_html=True)

erased_pct = int((1 - ((wheat_portion + corn_portion) / 2)) * 100)
st.markdown(f"## **{erased_pct}%** OF YOUR MEAL HAS BEEN **ERASED**")

# ==========================================
# 5. RIGOROUS ANALYSIS
# ==========================================
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌾 The Bread Crisis")
    st.write(f"Wheat is trading at **${mkt['Wheat']:.0f}**. Under **{escalation}**, logistics and fertilizer costs shrink the affordable portion by **{int((1-wheat_portion)*100)}%**.")

with col2:
    st.subheader("🍗 The Protein Tax")
    st.write(f"Corn (animal feed) prices are volatile. War-driven energy costs create a 'Hidden Tax' that erases **{int((1-corn_portion)*100)}%** of meat affordability.")

st.divider()
st.caption(f"© 2026 | Developed by Mohd Khairul Ridhuan | Worldwide Strategic Audit | Version 1.0")
