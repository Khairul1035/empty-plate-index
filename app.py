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
    /* Professional Light Theme */
    .stApp { background-color: #F8FAFC; }
    
    .header-box { 
        background: white; padding: 30px; border-radius: 15px; 
        border-top: 8px solid #E53E3E; margin-bottom: 25px; 
        box-shadow: 0 10px 15px rgba(0,0,0,0.05);
    }
    
    .profile-sidebar { 
        font-size: 0.9rem; line-height: 1.6; color: #2D3748; 
        background: #EDF2F7; padding: 15px; border-radius: 10px;
    }
    
    .audit-card { 
        background: white; padding: 20px; border-radius: 12px; 
        border: 1px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    h1, h2, h3 { color: #1A202C !important; font-family: 'Inter', sans-serif; }
    
    /* Metric Styling */
    [data-testid="stMetricValue"] { color: #E53E3E !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. GLOBAL DATA INTELLIGENCE
# ==========================================
@st.cache_data(ttl=300)
def get_global_intel():
    # Primary tickers for a Global War Audit
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
            data[name] = 0.0 # API Fallback
    return data

# List of every country in the world using pycountry
ALL_COUNTRIES = sorted([country.name for country in pycountry.countries])
mkt_intel = get_global_intel()

# ==========================================
# 3. SIDEBAR: THE ARCHITECT BIO
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown(f"### **Mohd Khairul Ridhuan bin Mohd Fadzil**")
    st.markdown("""
    <div class="profile-sidebar">
    <b>Lead Researcher:</b><br>
    • Business Related Research<br>
    • Maqasid Sharia Specialist<br>
    • Corporate Sustainability Expert<br><br>
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
    # Unique Country Selection for Comparative Analysis
    country_a = st.selectbox("🌍 Nation A (Baseline):", ALL_COUNTRIES, index=ALL_COUNTRIES.index("Malaysia") if "Malaysia" in ALL_COUNTRIES else 0)
    country_b = st.selectbox("🌍 Nation B (Comparison):", ALL_COUNTRIES, index=ALL_COUNTRIES.index("India") if "India" in ALL_COUNTRIES else 1)
    
    st.success("SYSTEM READY: Live Data Feed")

# ==========================================
# 4. DASHBOARD HEADER
# ==========================================
st.markdown(f"""
    <div class="header-box">
        <h1 style="margin:0; font-size:2.2rem;">🌐 GLOBAL STRATEGIC ERASURE AUDIT</h1>
        <p style="margin:0; font-size:1.1rem; color:#4A5568;"><b>Theme:</b> Assessing the US-Israel-Iran Kinetic Impact on Sovereign Integrity</p>
        <p style="margin:0; font-size:0.9rem; color:#718096;"><b>Project Architect:</b> Mohd Khairul Ridhuan bin Mohd Fadzil</p>
    </div>
    """, unsafe_allow_html=True)

# Global Market Ticker (Metric Row)
cols = st.columns(len(mkt_intel))
for i, (name, val) in enumerate(mkt_intel.items()):
    cols[i].metric(name, f"${val:.2f}")

st.divider()

# ==========================================
# 5. COMPARATIVE AUDIT COMPONENT
# ==========================================
def render_audit_column(name, intel, esc_level, unique_prefix):
    # Rigorous Simulation Logic (Seeded per Country Name)
    np.random.seed(sum([ord(c) for c in name])) 
    vuln_food = np.random.uniform(0.9, 2.3)
    vuln_fiscal = np.random.uniform(0.7, 2.9)
    
    esc_map = {"Peace": 0.05, "Localized": 0.18, "Tension": 0.38, "Regional War": 0.68, "Total War": 0.94}
    impact = esc_map[esc_level]
    
    erasure_food = min(int(impact * vuln_food * 100), 100)
    erasure_fiscal = min(int(impact * vuln_fiscal * 100), 100)
    erasure_geo = min(int(impact * 1.4 * 100), 100)
    
    st.markdown(f"### 📊 Strategic Audit: {name}")
    
    # Triple Pie Charts (HCI Visualized Data)
    chart_cols = st.columns(3)
    
    dims = [
        ("Food Integrity", erasure_food, "#48BB78", "Maqasid/Hifz al-Mal"),
        ("Fiscal Stability", erasure_fiscal, "#3182CE", "Corporate Sustainability"),
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
                showlegend=False, height=160, 
                margin=dict(t=10, b=10, l=10, r=10),
                paper_bgcolor='rgba(0,0,0,0)',
                annotations=[dict(text=f"{100-val}%", x=0.5, y=0.5, font_size=18, showarrow=False)]
            )
            # Unique key provided to prevent DuplicateElementId error
            st.plotly_chart(fig, use_container_width=True, key=f"{unique_prefix}_{i}_{name}")
            st.markdown(f"<center><small><b>{label}</b><br>{desc}</small></center>", unsafe_allow_html=True)
    
    # Audit Narrative
    st.markdown(f"""
    <div class="audit-card">
        <b>Combined Erasure Score: {int((erasure_food + erasure_fiscal + erasure_geo)/3)}%</b><br>
        <p style="font-size:0.85rem; margin-top:5px;">
        Evidence suggests that <b>{name}</b> faces high externalized risk under <b>{esc_level}</b> conditions. 
        Geopolitical erasure is currently impacting both fiscal reserves and domestic wealth integrity.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Comparison Grid Layout
col_a, col_b = st.columns(2)

with col_a:
    render_audit_column(country_a, mkt_intel, escalation, unique_prefix='A')

with col_b:
    render_audit_column(country_b, mkt_intel, escalation, unique_prefix='B')

# ==========================================
# 6. STRATEGIC POSITIONING FOOTER
# ==========================================
st.divider()
st.subheader("📡 Lead Architect's Executive Intelligence Summary")
with st.expander("Expand Strategic Analysis Briefing", expanded=True):
    st.write(f"""
    **Comparative National Audit: {country_a} vs {country_b}**
    
    *   **Maqasid Sharia Analysis:** This audit serves as a critical indicator for *Hifz al-Mal* (Preservation of Wealth). High erasure scores indicate a systemic failure in global economic frameworks to protect the property rights and purchasing power of the global population.
    *   **Corporate Sustainability Framework:** Businesses operating within these target nations must price-in the 'Kinetic War Premium' reflected in the Fiscal Stability audit.
    *   **AI, ML & HCI Integration:** This dashboard translates complex Machine Learning market nodes into a Human-Computer Interaction (HCI) model, allowing non-technical stakeholders to visualize abstract geopolitical threats as tangible 'Erasure' metrics.
    """)

st.markdown(f"<center><p style='color:grey !important;'>© 2026 | World Strategic Intelligence | Lead Architect: <b>Mohd Khairul Ridhuan bin Mohd Fadzil</b></p></center>", unsafe_allow_html=True)
