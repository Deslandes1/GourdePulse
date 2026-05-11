import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pytz
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="GLOBALINTERNET.PY | CAD High-Contrast", layout="wide")

# --- CUSTOM CSS FOR STRONG COLORS ---
st.markdown("""
    <style>
    .stApp { background: #000000; }
    
    /* Strong Color Styling for Metric Labels */
    [data-testid="stMetricLabel"] p {
        color: #FFD700 !important; /* Bright Gold for the Titles */
        font-size: 24px !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Strong Color Styling for Metric Values */
    [data-testid="stMetricValue"] {
        color: #00FF00 !important; /* Neon Green for the Numbers */
        font-size: 48px !important;
        font-weight: 900 !important;
        text-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
    }

    .title-glow { 
        font-size: 60px; font-weight: 900; color: #FFFFFF; 
        text-shadow: 0 0 30px #FF0000; text-align: center; 
    }
    
    .digital-clock { 
        background: #111; color: #FF0000; font-family: 'Courier New', monospace; 
        padding: 20px; border-radius: 10px; border: 2px solid #FF0000; 
        font-size: 20px; font-weight: bold; box-shadow: 0 0 20px rgba(255,0,0,0.4);
    }

    .footer { 
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #111; color: #FFD700 !important; 
        text-align: center; padding: 15px; font-weight: 900; 
        border-top: 3px solid #FF0000; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<h1 style="color:#FFD700;">COMMAND CENTER</h1>', unsafe_allow_html=True)
    clock_placeholder = st.empty()
    st.markdown("---")
    st.success("Gesner Deslandes")
    st.info("Lead Software Engineer")

# --- MAIN INTERFACE ---
st.markdown('<p class="title-glow">GLOBALINTERNET.PY</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Metric Columns
m_col1, m_col2, m_col3 = st.columns(3)
met1 = m_col1.empty()
met2 = m_col2.empty()
met3 = m_col3.empty()

chart_placeholder = st.empty()

# --- REFRESH LOOP ---
canada_tz = pytz.timezone('America/Toronto')
base_rate = 1.3625

while True:
    now_ca = datetime.now(canada_tz)
    
    # Update Clock
    clock_placeholder.markdown(f"""
        <div class="digital-clock">
            CANADA DATE: {now_ca.strftime('%d/%m/%Y')}<br>
            CANADA TIME: {now_ca.strftime('%H:%M:%S %p')}
        </div>
    """, unsafe_allow_html=True)

    # Market Flutter
    flutter = random.uniform(-0.0005, 0.0005)
    current_val = base_rate + flutter

    # INJECTING THE STRONG COLORED WRITINGS
    met1.metric(label="USD to CAD", value=f"{current_val:.4f}", delta=f"{flutter:.5f}")
    met2.metric(label="Market Health", value="94/100", delta="OPTIMAL")
    met3.metric(label="Volume (24h)", value="5.8B", delta="ACTIVE")

    # Chart logic
    df = pd.DataFrame({
        'Time': pd.date_range(end=now_ca, periods=20, freq='h'),
        'Value': [current_val + (random.uniform(-0.002, 0.002)) for _ in range(20)]
    })
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Time'], y=df['Value'], mode='lines+markers', 
                             line=dict(color='#FF0000', width=4),
                             marker=dict(color='#FFD700')))
    fig.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color="white"), height=400)
    chart_placeholder.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="footer">ENGINEERED BY GESNER DESLANDES | GLOBALINTERNET.PY 2026</div>', unsafe_allow_html=True)
    
    time.sleep(1)
