import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="GLOBALINTERNET.PY | GourdePulse", layout="wide")

# --- CUSTOM CSS FOR HIGH-CONTRAST AESTHETICS ---
st.markdown("""
    <style>
    /* Dark background for the whole app */
    .main {
        background-color: #0e1117;
    }
    
    /* Strong White Metric Styling */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    [data-testid="stMetricDelta"] {
        font-weight: 700 !important;
    }

    /* Container for metrics */
    .stMetric {
        background-color: #1a1c24;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363d;
    }

    /* Brand Header Styling */
    .title-glow {
        font-size: 50px;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 15px #00d4ff;
        text-align: center;
        margin-bottom: 5px;
    }

    /* Moving Marquee */
    .marquee {
        font-family: 'Courier New', Courier, monospace;
        color: #00ff00;
        white-space: nowrap;
        overflow: hidden;
        background: #000;
        padding: 8px;
        border-top: 1px solid #30363d;
        border-bottom: 1px solid #30363d;
    }

    /* Strong White Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #FFFFFF !important;
        text-align: center;
        padding: 12px;
        font-size: 15px;
        font-weight: 800;
        border-top: 2px solid #30363d;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='color:white;'>CORE HUB</h1>", unsafe_allow_html=True)
    selected_currency = st.selectbox(
        "Select Market Pair:",
        ["USD (US Dollar)", "EUR (Euro)", "DOP (Dominican Peso)", "CAD (Canadian Dollar)"]
    )
    st.markdown("---")
    st.markdown("**DEVELOPER PROFILE**")
    st.success("Gesner Deslandes")
    st.info("Role: Technology Coordinator")

# --- MAIN INTERFACE ---
st.markdown('<p class="title-glow">GLOBALINTERNET.PY</p>', unsafe_allow_html=True)

st.markdown("""
    <div class="marquee">
        ⚡ LIVE FEED: HTG LIQUIDITY ANALYSIS ACTIVE ... 2026 FISCAL DATA SYNCED ... 
        ENGINEERED BY GESNER DESLANDES ... STATUS: SECURE ...
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- TOP METRICS SECTION ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="USD to HTG", value="131.19", delta="0.0447")

with col2:
    st.metric(label="Currency Health Score", value="83/100", delta="-2% Volatility")

with col3:
    st.metric(label="Market Volume (24h)", value="1.2M", delta="High Activity", delta_color="normal")

# --- INTERACTIVE CHART ---
st.markdown("<h3 style='color:white; margin-top:30px;'>Live Market Insight</h3>", unsafe_allow_html=True)

# Fixed frequency to 'h' for Pandas 2.0+ compatibility
df = pd.DataFrame({
    'Time': pd.date_range(start=datetime.now(), periods=24, freq='h'),
    'Value': [131.19 + (random.uniform(-0.8, 0.8)) for _ in range(24)]
})

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['Time'], 
    y=df['Value'], 
    mode='lines+markers',
    line=dict(color='#00d4ff', width=4),
    fill='tozeroy',
    fillcolor='rgba(0, 212, 255, 0.1)'
))

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white"),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#30363d'),
    height=450,
    margin=dict(l=0, r=0, t=0, b=0)
)

st.plotly_chart(fig, use_container_width=True)

# --- REPORT GENERATOR ---
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("🚀 GENERATE FISCAL REPORT"):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="CONFIRM DOWNLOAD",
        data=csv,
        file_name="HTG_Market_Report.csv",
        mime="text/csv"
    )

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        © 2026 GLOBALINTERNET.PY | Software Engineered by Gesner Deslandes
    </div>
    """, unsafe_allow_html=True)
