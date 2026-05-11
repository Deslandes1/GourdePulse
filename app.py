import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pytz
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="GLOBALINTERNET.PY | Professional Engine", layout="wide")

# --- CSS FOR STRONG COLORS & SIDEBAR ---
st.markdown("""
    <style>
    .stApp { background: #000000; }
    
    /* STRONG COLOR WRITINGS FOR METRICS */
    [data-testid="stMetricLabel"] p {
        color: #FFD700 !important; /* Bright Gold for USD to CAD, Market Health, Volume */
        font-size: 22px !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }
    [data-testid="stMetricValue"] {
        color: #00FF00 !important; /* Neon Green for the Numbers */
        font-size: 45px !important;
        font-weight: 900 !important;
    }

    .title-glow { 
        font-size: 60px; font-weight: 900; color: #FFFFFF; 
        text-shadow: 0 0 25px #FF0000; text-align: center; 
    }
    
    .digital-clock { 
        background: #111; color: #FF0000; font-family: 'Courier New', monospace; 
        padding: 15px; border-radius: 8px; border: 2px solid #FF0000; 
        font-size: 18px; font-weight: bold; box-shadow: 0 0 15px rgba(255,0,0,0.3);
    }

    .footer { 
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #111; color: #FFFFFF !important; 
        text-align: center; padding: 10px; font-weight: 800; 
        border-top: 2px solid #FF0000; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CONSOLIDATED) ---
with st.sidebar:
    st.markdown('<h2 style="color:#FFD700; font-weight:900;">CORE HUB</h2>', unsafe_allow_html=True)
    
    # Live Clock Placeholder
    clock_placeholder = st.empty()
    
    st.markdown("---")
    st.markdown("**DEVELOPER PROFILE**")
    st.success("Gesner Deslandes")
    st.caption("🚀 Technology Coordinator | Lead Engineer")
    
    st.markdown("---")
    # THE ONLY DOWNLOAD FUNCTIONALITY AT THE END
    st.markdown('<p style="color:#FFD700; font-weight:bold;">FISCAL EXPORT</p>', unsafe_allow_html=True)
    download_placeholder = st.empty()

# --- MAIN INTERFACE ---
st.markdown('<p class="title-glow">GLOBALINTERNET.PY</p>', unsafe_allow_html=True)
st.markdown('<div style="background:#111; color:#00FF00; padding:10px; font-family:monospace; border-top:1px solid #FF0000;">⚡ LIVE FEED: USD/CAD ANALYSIS ACTIVE ... DATA SECURED ... ENGINEERED BY GESNER DESLANDES ...</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

m_col1, m_col2, m_col3 = st.columns(3)
met1, met2, met3 = m_col1.empty(), m_col2.empty(), m_col3.empty()

chart_placeholder = st.empty()

# --- ENGINE LOGIC ---
canada_tz = pytz.timezone('America/Toronto')
base_usd_cad = 1.3625

while True:
    now_ca = datetime.now(canada_tz)
    
    # 1. Update Clock
    clock_placeholder.markdown(f"""
        <div class="digital-clock">
            DATE: {now_ca.strftime('%d/%m/%Y')}<br>
            TIME: {now_ca.strftime('%H:%M:%S %p')}
        </div>
    """, unsafe_allow_html=True)

    # 2. Update Metrics with STRONG COLORS
    flutter = random.uniform(-0.0006, 0.0006)
    current_val = base_usd_cad + flutter
    
    met1.metric(label="USD to CAD", value=f"{current_val:.4f}", delta=f"{flutter:.5f}")
    met2.metric(label="Market Health", value="92/100", delta="STABLE")
    met3.metric(label="Volume (24h)", value="5.1B", delta="LIVE")

    # 3. Update Chart
    df = pd.DataFrame({
        'Time': pd.date_range(end=now_ca, periods=20, freq='h'),
        'Value': [current_val + (random.uniform(-0.003, 0.003)) for _ in range(20)]
    })
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Time'], y=df['Value'], mode='lines', line=dict(color='#FF0000', width=4), fill='tozeroy', fillcolor='rgba(255, 0, 0, 0.1)'))
    fig.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color="white"), height=400, margin=dict(l=0, r=0, t=0, b=0))
    chart_placeholder.plotly_chart(fig, use_container_width=True)

    # 4. Update the Single Download Report at the bottom
    report_df = pd.DataFrame({
        "Report ID": [f"CAD-SYNC-{random.randint(1000, 9999)}"],
        "Timestamp": [now_ca.strftime('%Y-%m-%d %H:%M:%S')],
        "Pair": ["USD/CAD"],
        "Rate": [current_val],
        "Engineer": ["Gesner Deslandes"]
    })
    csv_data = report_df.to_csv(index=False).encode('utf-8')
    download_placeholder.download_button(
        label="📥 DOWNLOAD FISCAL REPORT",
        data=csv_data,
        file_name=f"GLOBALINTERNET_CAD_{now_ca.strftime('%H%M%S')}.csv",
        mime="text/csv"
    )

    st.markdown('<div class="footer">© 2026 GLOBALINTERNET.PY | SOFTWARE ENGINEERED BY GESNER DESLANDES</div>', unsafe_allow_html=True)
    time.sleep(1)
