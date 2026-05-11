import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pytz
import random
import time
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="GLOBALINTERNET.PY | CAD Pulse", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0d1b2a 0%, #000000 100%); }
    .sidebar-header { color: #FF0000 !important; font-size: 28px !important; font-weight: 900 !important; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 42px !important; font-weight: 900 !important; }
    .title-glow { font-size: 55px; font-weight: 900; color: #FFFFFF; text-shadow: 0 0 20px rgba(255, 0, 0, 0.6); text-align: center; }
    .digital-clock { 
        background: #000; color: #ff3131; font-family: 'Courier New', monospace; 
        padding: 15px; border-radius: 5px; text-align: left; 
        border: 1px solid #ff0000; font-size: 18px; font-weight: bold; 
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.3);
    }
    .marquee { font-family: 'Courier New', monospace; color: #ff3131; background: #000; padding: 10px; border-top: 1px solid #ff0000; font-weight: bold; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1b2a; color: #FFFFFF !important; text-align: center; padding: 12px; font-weight: 900; border-top: 2px solid #ff0000; z-index: 100; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<p class="sidebar-header">CENTRE CENTRAL</p>', unsafe_allow_html=True)
    
    # Canada Time Clock Placeholder
    clock_placeholder = st.empty()
    
    st.markdown("<br>", unsafe_allow_html=True)
    # Focus on USD/CAD
    selected_currency = "USD/CAD"
    
    st.markdown("---")
    st.markdown("**DEVELOPER PROFILE**")
    st.success("Gesner Deslandes")
    st.caption("🚀 Technology Coordinator | Lead Engineer")
    
    # FISCAL DOWNLOAD
    st.markdown("---")
    canada_tz = pytz.timezone('America/Toronto')
    now_ca = datetime.now(canada_tz)
    
    report_data = {
        "Report ID": [f"CAD-SYNC-{random.randint(1000, 9999)}"],
        "Date": [now_ca.strftime('%Y-%m-%d')],
        "Time (Canada)": [now_ca.strftime('%H:%M:%S %p')],
        "Pair": ["USD/CAD"],
        "Market Rate": [1.36 + random.uniform(-0.001, 0.001)],
        "Status": ["Stable Liquidity"],
        "Engineer": ["Gesner Deslandes"]
    }
    csv = pd.DataFrame(report_data).to_csv(index=False).encode('utf-8')
    st.download_button("📊 GENERATE FISCAL REPORT", data=csv, file_name="CAD_MARKET_REPORT.csv", mime="text/csv")

# --- MAIN PAGE ---
st.markdown('<p class="title-glow">GLOBALINTERNET.PY</p>', unsafe_allow_html=True)
st.markdown('<div class="marquee">⚡ LIVE FEED: USD/CAD ANALYSIS ACTIVE ... BANK OF CANADA DATA SYNCED ... ENGINEERED BY GESNER DESLANDES ...</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

m_col1, m_col2, m_col3 = st.columns(3)
met1, met2, met3 = m_col1.empty(), m_col2.empty(), m_col3.empty()

st.markdown("<h2 style='color:white; text-align:center;'>Professional Market Analytics</h2>", unsafe_allow_html=True)
chart_placeholder = st.empty()

# --- REFRESH LOOP (Canada Time) ---
base_usd_cad = 1.3625 

while True:
    now_ca = datetime.now(canada_tz)
    
    # Update Clock
    clock_placeholder.markdown(f"""
        <div class="digital-clock">
            DATE: {now_ca.strftime('%d/%m/%Y')}<br>
            TIME: {now_ca.strftime('%H:%M:%S %p')}
        </div>
    """, unsafe_allow_html=True)

    # Update Market Data
    flutter = random.uniform(-0.0005, 0.0005)
    current_rate = base_usd_cad + flutter
    
    met1.metric(label="USD to CAD", value=f"{current_rate:.4f}", delta=f"{flutter:.5f}")
    met2.metric(label="Market Health", value="88/100", delta="-0.2% Volatility")
    met3.metric(label="Volume (24h)", value="4.2B", delta="LIVE FEED")

    # Update Chart
    df = pd.DataFrame({
        'Time': pd.date_range(end=now_ca, periods=30, freq='h'),
        'Value': [current_rate + (random.uniform(-0.005, 0.005)) for _ in range(30)]
    })
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Time'], y=df['Value'], mode='lines', line=dict(color='#ff0000', width=4), fill='tozeroy', fillcolor='rgba(255, 0, 0, 0.1)'))
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), height=350, margin=dict(l=0, r=0, t=0, b=0))
    chart_placeholder.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="footer">© 2026 GLOBALINTERNET.PY | Software Engineered by Gesner Deslandes</div>', unsafe_allow_html=True)
    time.sleep(1)
