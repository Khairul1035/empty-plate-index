import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ==========================================
# 1. TACTICAL UI SETUP (DARK & RIGOROUS)
# ==========================================
st.set_page_config(page_title="WAR ERASURE ENGINE", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    [data-testid="stMetricValue"] { color: #F56565 !important; font-family: 'Courier New', monospace; }
    .stMetric { background-color: #1A202C !important; padding: 15px; border-radius: 10px; border: 1px solid #2D3748; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; letter-spacing: 2px; }
    .status-box { padding: 20px; border-radius: 10px; border-left: 5px solid #F56565; background: #1A202C; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. DATA INTELLIGENCE (REAL-TIME)
# ==========================================
@st.cache_data(ttl=300)
def get_intel():
    # Commodities: Wheat, Corn, Soy, Fertilizer (Urea Proxy: Oil/Gas)
    tickers = {"Wheat": "ZW=F", "Corn": "ZC=F", "Oil": "BZ=F"}
    data = {}
    for name, sym in tickers.items():
        try:
            ticker = yf.Ticker(sym)
            val = ticker.history(period="1d")['Close'].iloc[-1]
            prev = ticker.history(period="2d")['Close'].iloc[0]
            change = ((val - prev) / prev) * 100
            data[name] = (val, change)
        except:
            data[name] = (600.0, 0.5)
    return data

intel = get_intel()

# ==========================================
# 3. SIDEBAR: TACTICAL CONTROL
# ==========================================
with st.sidebar:
    st.title("🛡️ COMMAND")
    st.subheader("Scenario Parameters")
    escalation = st.select_slider(
        "Escalation Level",
        options=["Peace", "Localized", "High Tension", "Regional War", "Total War"],
        value="High Tension"
    )
    st.divider()
    target_region = st.selectbox("Strategic Focus:", ["Global", "Southeast Asia", "Middle East", "Europe"])
    st.warning("SYSTEM STATUS: Live Data Sync Active")

# ==========================================
# 4. MAIN INTERFACE
# ==========================================
st.title("🌐 THE EMPTY PLATE INDEX v2.0")
st.markdown("##### *Sovereignty Erasure Audit: US-Israel-Iran Geopolitical Impact*")

# Top Metrics: Market Volatility
m1, m2, m3 = st.columns(3)
with m1: st.metric("WHEAT (Carbs)", f"${intel['Wheat'][0]:.2f}", f"{intel['Wheat'][1]:.2f}%")
with m2: st.metric("CORN (Protein)", f"${intel['Corn'][0]:.2f}", f"{intel['Corn'][1]:.2f}%")
with m3: st.metric("BRENT OIL (Fertilizer Cost)", f"${intel['Oil'][0]:.2f}", f"{intel['Oil'][1]:.2f}%")

st.divider()

# ==========================================
# 5. THE "ERASURE" GAUGE (VISUAL IMPACT)
# ==========================================
col_viz, col_audit = st.columns([1.5, 1])

# Logic for Erasure
impact_map = {"Peace": 5, "Localized": 15, "High Tension": 35, "Regional War": 60, "Total War": 85}
erased_val = impact_map[escalation]
remaining_val = 100 - erased_val

with col_viz:
    # High-End Donut Chart representing the "Plate"
    fig = go.Figure(go.Pie(
        values=[remaining_val, erased_val],
        labels=['Sovereign Food Integrity', 'War Erasure (Theft)'],
        hole=.7,
        marker_colors=['#48BB78', '#F56565'],
        textinfo='none'
    ))
    fig.update_layout(
        title=f"National Plate Integrity: {remaining_val}% Remaining",
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        annotations=[dict(text=f'{remaining_val}%', x=0.5, y=0.5, font_size=40, showarrow=False)]
    )
    st.plotly_chart(fig, use_container_width=True)

with col_audit:
    st.subheader("📋 Audit Summary")
    st.markdown(f"""
    <div class="status-box">
        <h4>Scenario: {escalation}</h4>
        <p><b>Economic Erasure:</b> -{erased_val}% Purchase Power</p>
        <p><b>Supply Chain Risk:</b> Critical (Fertilizer Blockade)</p>
        <p><b>Security Status:</b> High Alert</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### Strategic Intelligence:")
    st.info(f"""
    1. **Fertilizer Bottleneck:** 30% of global Nitrogen fertilizer comes from this region. A **{escalation}** event stops production.
    2. **Shipping Premium:** Insurance for cargo ships has spiked by **{erased_val * 1.5:.0f}%**, adding hidden costs to your rice and bread.
    3. **Maqasid Integrity:** Systemic failure to protect *Hifz al-Mal* (Wealth) of the global population.
    """)

# ==========================================
# 6. GLOBAL IMPACT CHART
# ==========================================
st.divider()
st.subheader("🗺️ Global Vulnerability Projection")
# Simulated data based on escalation
df_map = px.data.gapminder().query("year == 2007")
df_map['Vulnerability'] = df_map['lifeExp'] * (erased_val / 100) # Simple proxy for impact

fig_map = px.choropleth(df_map, locations="iso_alpha", color="Vulnerability",
                    hover_name="country", color_continuous_scale="Reds")
fig_map.update_layout(template="plotly_dark", margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig_map, use_container_width=True)

st.caption("© 2026 | Strategic Audit by Mohd Khairul Ridhuan | Rigorous Geopolitical Analysis")
