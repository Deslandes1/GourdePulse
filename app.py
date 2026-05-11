import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="GLOBALINTERNET.PY | GourdePulse", layout="wide")

# --- TRANSLATION DICTIONARY ---
languages = {
    "English": {
        "core_hub": "CORE HUB",
        "select_pair": "Select Market Pair:",
        "dev_profile": "DEVELOPER PROFILE",
        "role": "Engineer in Chief at GlobalInternet.py",
        "marquee": "⚡ LIVE FEED: HTG LIQUIDITY ANALYSIS ACTIVE ... 2026 FISCAL DATA SYNCED ... ENGINEERED BY GESNER DESLANDES ...",
        "health": "Currency Health Score",
        "volatility": "Volatility",
        "volume": "Market Volume (24h)",
        "insight": "Professional Market Analytics",
        "signal": "Market Signal",
        "btn_report": "🚀 GENERATE FISCAL REPORT",
        "confirm": "CONFIRM DOWNLOAD"
    },
    "Français": {
        "core_hub": "CENTRE CENTRAL",
        "select_pair": "Sélectionner la Paire:",
        "dev_profile": "PROFIL DU DÉVELOPPEUR",
        "role": "Ingénieur en Chef chez GlobalInternet.py",
        "marquee": "⚡ FLUX EN DIRECT: ANALYSE DE LIQUIDITÉ HTG ACTIVE ... DONNÉES FISCALES 2026 ... CONÇU PAR GESNER DESLANDES ...",
        "health": "Score de Santé de la Devise",
        "volatility": "Volatilité",
        "volume": "Volume du Marché (24h)",
        "insight": "Analytique Professionnelle du Marché",
        "signal": "Signal du Marché",
        "btn_report": "🚀 GÉNÉRER LE RAPPORT FISCAL",
        "confirm": "CONFIRMER LE TÉLÉCHARGEMENT"
    },
    "Kreyòl Ayisyen": {
        "core_hub": "HUB PRENSIPAL",
        "select_pair": "Chwazi Pè Lajan:",
        "dev_profile": "PWOFIL DEVLOPÈ A",
        "role": "Enjenyè an Chèf nan GlobalInternet.py",
        "marquee": "⚡ LIVE FEED: ANALIZ LIKIDITE HTG AKTIF ... DONE FISKAL 2026 ... GESNER DESLANDES TE BWASE PWOJÈ SA ...",
        "health": "Sante Lajan an",
        "volatility": "Volatilite",
        "volume": "Volim Mache a (24h)",
        "insight": "Analiz Pwofesyonèl Mache a",
        "signal": "Siyal Mache",
        "btn_report": "🚀 JENERE RAPÒ FISKAL",
        "confirm": "KONFIME TELECHAJMAN"
    }
}

# --- CUSTOM CSS FOR "ATTRACTIVELY BEAUTIFUL" UI ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    
    /* CORE HUB - High Visibility Gold */
    .sidebar-header {
        color: #FFD700 !important;
        font-size: 28px !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.3);
        margin-bottom: 5px;
    }

    /* Strong White Metrics */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 42px !important;
        font-weight: 900 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* Glassmorphism Insight Card */
    .insight-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    .title-glow {
        font-size: 55px;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 20px #00d4ff;
        text-align: center;
        margin-bottom: 0px;
    }

    .marquee {
        font-family: 'Courier New', Courier, monospace;
        color: #00ff00;
        background: #000;
        padding: 10px;
        border-top: 1px solid #30363d;
        font-weight: bold;
    }

    .footer {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background-color: #0e1117;
        color: #FFFFFF !important;
        text-align: center;
        padding: 12px;
        font-weight: 800;
        border-top: 2px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    lang_choice = st.selectbox("🌐 Choose Language", ["English", "Français", "Kreyòl Ayisyen"])
    t = languages[lang_choice]
    
    st.markdown(f'<p class="sidebar-header">{t["core_hub"]}</p>', unsafe_allow_html=True)
    
    selected_currency = st.selectbox(t["select_pair"], ["USD", "EUR", "DOP", "CAD"])
    
    st.markdown("---")
    st.markdown(f"**{t['dev_profile']}**")
    st.success("Gesner Deslandes")
    st.caption(f"🚀 {t['role']}")
    st.info("Status: 🟢 System Online")

# --- MAIN INTERFACE ---
st.markdown('<p class="title-glow">GLOBALINTERNET.PY</p>', unsafe_allow_html=True)
st.markdown(f'<div class="marquee">{t["marquee"]}</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- TOP METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label=f"{selected_currency} to HTG", value="131.19", delta="0.0447")
with col2:
    st.metric(label=t["health"], value="83/100", delta=f"-2% {t['volatility']}")
with col3:
    st.metric(label=t["volume"], value="1.2M", delta="High Activity")

# --- ENHANCED INSIGHT BOARD (THE RE-DESIGN) ---
st.markdown(f"<h2 style='color:white; text-align:center;'>{t['insight']}</h2>", unsafe_allow_html=True)

chart_col, signal_col = st.columns([3, 1])

# Data for Chart
df = pd.DataFrame({
    'Time': pd.date_range(start=datetime.now(), periods=30, freq='h'),
    'Value': [131.19 + (random.uniform(-1.2, 1.2)) for _ in range(30)]
})

with chart_col:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Time'], y=df['Value'],
        mode='lines',
        line=dict(color='#00d4ff', width=5),
        fill='tozeroy',
        fillcolor='rgba(0, 212, 255, 0.15)'
    ))
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#2e313d')
    )
    st.plotly_chart(fig, use_container_width=True)

with signal_col:
    st.markdown(f"""
    <div class="insight-card">
        <h4 style="color:white; margin-bottom:10px;">{t['signal']}</h4>
        <p style="color:#00ff00; font-size:24px; font-weight:bold;">STRONG BUY</p>
        <hr style="border-color:rgba(255,255,255,0.1);">
        <p style="color:white; font-size:14px;">Resistance: 133.50</p>
        <p style="color:white; font-size:14px;">Support: 129.10</p>
        <p style="color:#00d4ff; font-size:12px; margin-top:20px;">Powered by GlobalInternet Logic</p>
    </div>
    """, unsafe_allow_html=True)

# --- REPORT & FOOTER ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button(t["btn_report"]):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label=t["confirm"], data=csv, file_name="HTG_Market_Intelligence.csv", mime="text/csv")

st.markdown(f"""
    <div class="footer">
        © 2026 GLOBALINTERNET.PY | Software Engineered by Gesner Deslandes
    </div>
    """, unsafe_allow_html=True)
