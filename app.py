import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="GLOBALINTERNET.PY | Currency Tracker", layout="wide")

# --- CUSTOM CSS FOR SOCIAL MEDIA AESTHETICS ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1a1c24;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #2e313d;
        box-shadow: 0 4px 15px rgba(0,255,255,0.1);
    }
    .title-glow {
        font-size: 45px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff;
        text-align: center;
        margin-bottom: 10px;
    }
    .marquee {
        font-family: 'Courier New', Courier, monospace;
        color: #00ff00;
        white-space: nowrap;
        overflow: hidden;
        background: #000;
        padding: 5px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #555;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #2e313d;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR & CURRENCY SELECTION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2091/2091665.png", width=100)
    st.markdown("## Global Settings")
    
    selected_currency = st.selectbox(
        "Compare HTG Against:",
        ["USD (US Dollar)", "EUR (Euro)", "DOP (Dominican Peso)", "CAD (Canadian Dollar)", "BRL (Brazilian Real)"]
    )
    
    st.markdown("---")
    st.write("**Developer:**")
    st.info("Gesner Deslandes")
    st.write("**Status:** 🟢 Live Market Feed")

# --- HEADER SECTION ---
st.markdown('<p class="title-glow">GLOBALINTERNET.PY</p>', unsafe_allow_html=True)
st.markdown("""
    <div class="marquee">
        📈 HTG STABILITY INDEX: ACTIVE ... MARKET DATA FLOWING ... CONNECTIVITY SECURED ... 
        SYSTEM STATUS: NOMINAL ... DEVELOPED BY GESNER DESLANDES ...
    </div>
    """, unsafe_allow_html=True)

# --- MOCK LIVE DATA LOGIC ---
# In a real app, you'd call an API here. We'll simulate movement for the video.
base_rates = {"USD": 131.25, "EUR": 142.10, "DOP": 2.22, "CAD": 96.40, "BRL": 26.15}
current_code = selected_currency.split(" ")[0]
current_rate = base_rates[current_code] + random.uniform(-0.5, 0.5)

# --- METRIC DISPLAY ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label=f"1 {current_code} to HTG", value=f"{current_rate:.2f}", delta=f"{random.uniform(-0.1, 0.1):.4f}")

with col2:
    health_score = random.randint(65, 85)
    st.metric(label="Currency Health Score", value=f"{health_score}/100", delta="-2% Volatility")

with col3:
    st.metric(label="Market Volume (24h)", value="1.2M", delta="High Activity")

# --- LIVE CHART ---
st.markdown("### Market Behavior Insight")
df = pd.DataFrame({
    'Time': pd.date_range(start='now', periods=20, freq='H'),
    'Rate': [current_rate + random.uniform(-1, 1) for _ in range(20)]
})

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Time'], y=df['Rate'], mode='lines+markers', 
                         line=dict(color='#00d4ff', width=3),
                         fill='tozeroy', fillcolor='rgba(0, 212, 255, 0.1)'))

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white"),
    margin=dict(l=0, r=0, t=0, b=0),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#2e313d')
)

st.plotly_chart(fig, use_container_運width=True)

# --- DOWNLOAD SECTION ---
st.markdown("---")
st.markdown("### Generate Intelligence Report")
if st.button(f"Download {current_code}/HTG Performance Report"):
    report_data = df.to_csv().encode('utf-8')
    st.download_button(
        label="Click to confirm CSV Download",
        data=report_data,
        file_name=f"HTG_{current_code}_Report.csv",
        mime="text/csv"
    )

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        © {datetime.now().year} GLOBALINTERNET.PY | Software Engineered by Gesner Deslandes
    </div>
    """, unsafe_allow_html=True)
