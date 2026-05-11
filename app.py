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
        "select_lang": "Select Language:",
        "select_pair": "Select Market Pair:",
        "dev_profile": "DEVELOPER PROFILE",
        "role": "Role: Technology Coordinator",
        "marquee": "⚡ LIVE FEED: HTG LIQUIDITY ANALYSIS ACTIVE ... 2026 FISCAL DATA SYNCED ... ENGINEERED BY GESNER DESLANDES ...",
        "health": "Currency Health Score",
        "volatility": "Volatility",
        "volume": "Market Volume (24h)",
        "insight": "Live Market Insight",
        "btn_report": "🚀 GENERATE FISCAL REPORT",
        "confirm": "CONFIRM DOWNLOAD"
    },
    "Français": {
        "core_hub": "CENTRE CENTRAL",
        "select_lang": "Choisir la Langue:",
        "select_pair": "Sélectionner la Paire:",
        "dev_profile": "PROFIL DU DÉVELOPPEUR",
        "role": "Rôle: Coordonnateur Technologique",
        "marquee": "⚡ FLUX EN DIRECT: ANALYSE DE LIQUIDITÉ HTG ACTIVE ... DONNÉES FISCALES 2026 ... CONÇU PAR GESNER DESLANDES ...",
        "health": "Score de Santé de la Devise",
        "volatility": "Volatilité",
        "volume": "Volume du Marché (24h)",
        "insight": "Aperçu du Marché en Direct",
        "btn_report": "🚀 GÉNÉRER LE RAPPORT FISCAL",
        "confirm": "CONFIRMER LE TÉLÉCHARGEMENT"
    },
    "Kreyòl Ayisyen": {
        "core_hub": "HUB PRENSIPAL",
        "select_lang": "Chwazi Lang:",
        "select_pair": "Chwazi Pè Lajan:",
        "dev_profile": "PWOFIL DEVLOPÈ A",
        "role": "Wòl: Kòdonatè Teknoloji",
        "marquee": "⚡ LIVE FEED: ANALIZ LIKIDITE HTG AKTIF ... DONE FISKAL 2026 ... GESNER DESLANDES TE BWASE PWOJÈ SA ...",
        "health": "Sante Lajan an",
        "volatility": "Volatilite",
        "volume": "Volim Mache a (24h)",
        "insight": "Done Mache a an Dirèk",
        "btn_report": "🚀 JENERE RAPÒ FISKAL",
        "confirm": "KONFIME TELECHAJMAN"
    }
}

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    
    /* Core Hub - Specialized Gold Color */
    .sidebar-header {
        color: #FFD700 !important;
        font-size: 28px !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 38px !important;
        font-weight: 900 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }
    .title-glow {
        font-size: 50px;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 15px #00d4ff;
        text-align: center;
    }
    .marquee {
        font-family: 'Courier New', Courier, monospace;
        color: #00ff00;
        background: #000;
        padding: 8px;
        border-top: 1px solid #30363d;
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

# --- SIDEBAR & LANGUAGE SELECTION ---
with st.sidebar:
    lang_choice = st.selectbox("🌐 Language / Lang / Langue", ["English", "Français", "Kreyòl Ayisyen"])
    t = languages[lang_choice]
    
    st.markdown(f'<p class="sidebar-header">{t["core_hub"]}</p>', unsafe_allow_html=True)
    
    selected_currency = st.selectbox(
        t["select_pair"],
        ["USD", "EUR", "DOP", "CAD"]
    )
    st.markdown("---")
    st.markdown(f"**{t['dev_profile']}**")
    st.success("Gesner Deslandes")
    st.info(t["role"])

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

# --- CHART ---
st.markdown(f"<h3 style='color:white;'>{t['insight']}</h3>", unsafe_allow_html=True)

df = pd.DataFrame({
    'Time': pd.date_range(start=datetime.now(), periods=24, freq='h'),
    'Value': [131.19 + (random.uniform(-0.8, 0.8)) for _ in range(24)]
})

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Time'], y=df['Value'], mode='lines', line=dict(color='#00d4ff', width=4), fill='tozeroy'))
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), height=400)
st.plotly_chart(fig, use_container_width=True)

# --- REPORT ---
if st.button(t["btn_report"]):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label=t["confirm"], data=csv, file_name="HTG_Report.csv", mime="text/csv")

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        © 2026 GLOBALINTERNET.PY | Software Engineered by Gesner Deslandes
    </div>
    """, unsafe_allow_html=True)
