import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pytz
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="GLOBALINTERNET.PY | Live GourdePulse", layout="wide")

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

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #1a0b2e 0%, #0e1117 100%); }
    .sidebar-header { color: #FFD700 !important; font-size: 28px !important; font-weight: 900 !important; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 42px !important; font-weight: 900 !important; }
    [data-testid="stMetricLabel"] { color: #FFFFFF !important; font-weight: 800 !important; }
    .title-glow { font-size: 55px; font-weight: 900; color: #FFFFFF; text-shadow: 0 0 20px rgba(162, 89, 255, 0.8); text-align: center; }
    .digital-clock { 
        background: #000; color: #00ff00; font-family: 'Courier New', monospace; 
        padding: 15px; border-radius: 5px; text-align: left; 
        border: 1px solid #a259ff; font-size: 18px; font-weight: bold; 
        box-shadow: 0 0 15px rgba(162, 89, 255, 0.3);
    }
    .marquee { font-family: 'Courier New', monospace; color: #00ff00; background: #000; padding: 10px; border-top: 1px solid #a259ff; font-weight: bold; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #1a0b2e; color: #FFFFFF !important; text-align: center; padding: 12px; font-weight: 900; border-top: 2px solid #a259ff; z-index: 100; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    lang_choice = st.selectbox("🌐 Language Selection", ["English", "Français", "Kreyòl Ayisyen"])
    t = languages[lang_choice]
    st.markdown(f'<p class="sidebar-header">{t["core_hub"]}</p>', unsafe_allow_html=True)
    
    clock_placeholder = st.empty()
    
    st.markdown("<br>", unsafe_allow_html=True)
    selected_currency = st.selectbox(t["select_pair"], ["USD", "EUR", "DOP", "CAD"])
    
    st.markdown("---")
    st.markdown(f"**{t['dev_profile']}**")
    st.success("Gesner Deslandes")
    st.caption(f"🚀 {t['role']}")

# --- MAIN PAGE PLACEHOLDERS ---
st.markdown('<p class="title-glow">GLOBALINTERNET.PY</p>', unsafe_allow_html=True)
st.markdown(f'<div class="marquee">{t["marquee"]}</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Metric Placeholders
m_col1, m_col2, m_col3 = st.columns(3)
met1 = m_col1.empty()
met2 = m_col2.empty()
met3 = m_col3.empty()

# Chart Placeholder
st.markdown(f"<h2 style='color:white; text-align:center;'>{t['insight']}</h2>", unsafe_allow_html=True)
chart_placeholder = st.empty()

# --- HAITI TIME & MARKET REFRESH LOOP ---
haiti_tz = pytz.timezone('America/Port-au-Prince')
base_htg = 131.19
multipliers = {"USD": 1.0, "EUR": 1.08, "DOP": 0.017, "CAD": 0.74}

while True:
    # 1. Update Time
    haiti_now = datetime.now(haiti_tz)
    time_string = haiti_now.strftime('%H:%M:%S %p')
    date_string = haiti_now.strftime('%d/%m/%Y')
    
    clock_placeholder.markdown(f"""
        <div class="digital-clock">
            DATE: {date_string}<br>
            TIME: {time_string}
        </div>
    """, unsafe_allow_html=True)

    # 2. Update Market Data (Live Flutter)
    live_flutter = random.uniform(-0.03, 0.03)
    final_rate = (base_htg * multipliers[selected_currency]) + live_flutter
    
    # Update Metrics in real-time
    met1.metric(label=f"{selected_currency} to HTG", value=f"{final_rate:.2f}", delta=f"{live_flutter:.4f}")
    met2.metric(label=t["health"], value=f"{random.randint(82, 84)}/100", delta=f"{random.uniform(-1.5, -2.5):.1f}% {t['volatility']}")
    met3.metric(label=t["volume"], value=f"{random.uniform(1.2, 1.3):.1f}M", delta="LIVE FEED")

    # 3. Update Chart in real-time
    df = pd.DataFrame({
        'Time': pd.date_range(end=haiti_now, periods=30, freq='h'),
        'Value': [final_rate + (random.uniform(-1, 1)) for _ in range(30)]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Time'], y=df['Value'], mode='lines', line=dict(color='#a259ff', width=5), fill='tozeroy', fillcolor='rgba(162, 89, 255, 0.1)'))
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), height=350, margin=dict(l=0, r=0, t=0, b=0), xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='rgba(162, 89, 255, 0.1)'))
    
    chart_placeholder.plotly_chart(fig, use_container_width=True)

    # Footer stays static at bottom
    st.markdown(f"""
        <div class="footer">
            © 2026 GLOBALINTERNET.PY | Software Engineered by Gesner Deslandes
        </div>
        """, unsafe_allow_html=True)

    time.sleep(1) # Re-run the entire dashboard logic every 1 second
