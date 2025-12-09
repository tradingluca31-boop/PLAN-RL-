"""
GUIDE OPTUNA COMPLET - Trading RL Gold
Version PRO avec design moderne et checkboxes interactifs
"""

import streamlit as st

st.set_page_config(
    page_title="Guide Optuna - RL Trading Gold",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'progress' not in st.session_state:
    st.session_state.progress = {
        'indicateurs': False,
        'sltp': False,
        'volatilite': False,
        'features': False,
        'temporels': False,
        'rewards': False,
        'architecture': False,
        'rl_params': False
    }

# CSS pour design moderne
st.markdown("""
<style>
    /* Header principal */
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    .main-header h1 {
        color: #ffd700;
        font-size: 3rem;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .main-header p {
        color: #e8e8e8;
        font-size: 1.3rem;
    }

    /* Cards de phase */
    .phase-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f5);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    .phase-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
    }
    .phase-card-done {
        background: linear-gradient(145deg, #e8f5e9, #c8e6c9);
        border: 2px solid #4caf50;
    }
    .phase-card-pending {
        background: linear-gradient(145deg, #fff3e0, #ffe0b2);
        border: 2px solid #ff9800;
    }

    /* Titres de phase */
    .phase-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .phase-number {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 700;
    }

    /* TOP 3 box */
    .top3-box {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    .top3-box h4 {
        color: #ffd700;
        margin-bottom: 10px;
        font-size: 1.1rem;
    }
    .top3-box p {
        margin: 5px 0;
        font-size: 0.95rem;
    }

    /* Progress bar custom */
    .progress-container {
        background: #e0e0e0;
        border-radius: 25px;
        height: 40px;
        margin: 20px 0;
        overflow: hidden;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.1);
    }
    .progress-bar {
        background: linear-gradient(90deg, #4caf50, #8bc34a);
        height: 100%;
        border-radius: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        transition: width 0.5s ease;
    }

    /* Metrics cards */
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffd700;
    }
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 5px;
    }

    /* Checkbox styling */
    .stCheckbox > label {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }

    /* Status badges */
    .status-done {
        background: linear-gradient(135deg, #4caf50, #8bc34a);
        color: white;
        padding: 8px 20px;
        border-radius: 25px;
        font-weight: 700;
        font-size: 1rem;
        display: inline-block;
    }
    .status-pending {
        background: linear-gradient(135deg, #ff9800, #ffc107);
        color: #1a1a2e;
        padding: 8px 20px;
        border-radius: 25px;
        font-weight: 700;
        font-size: 1rem;
        display: inline-block;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="main-header">
    <h1>🏆 GUIDE OPTUNA COMPLET</h1>
    <p>Optimisation Professionnelle pour Agent RL Trading Gold</p>
    <p style="color: #ffd700; font-weight: 600;">NIVEAU INSTITUTIONNEL</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# METRICS
# ============================================================================
completed = sum(st.session_state.progress.values())
total = len(st.session_state.progress)
progress_pct = int((completed / total) * 100)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">150+</div>
        <div class="metric-label">Parametres</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">8</div>
        <div class="metric-label">Categories</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{completed}/8</div>
        <div class="metric-label">Phases Terminees</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">~48h</div>
        <div class="metric-label">Temps Total</div>
    </div>
    """, unsafe_allow_html=True)

# Progress bar
st.markdown(f"""
<div class="progress-container">
    <div class="progress-bar" style="width: {max(progress_pct, 5)}%;">
        {progress_pct}% Complete
    </div>
</div>
""", unsafe_allow_html=True)

if completed == 8:
    st.balloons()
    st.success("🎉 **TOUTES LES PHASES TERMINEES!** Pret pour le TRAINING FINAL (1.5M steps)")

st.markdown("---")

# ============================================================================
# PHASES AVEC CHECKBOXES
# ============================================================================
st.markdown("## 📋 PHASES D'OPTIMISATION")
st.markdown("##### Cochez chaque phase une fois terminee")

# Phase 1: Indicateurs
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['indicateurs'] = st.checkbox(
        "", value=st.session_state.progress['indicateurs'], key="cb1"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['indicateurs'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['indicateurs'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">1</span>
            INDICATEURS TECHNIQUES
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 RSI Period</h4>
                <p><strong>Range:</strong> 5 - 30</p>
                <p><strong>Default:</strong> 14</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 MACD Fast/Slow</h4>
                <p><strong>Fast:</strong> 8 - 15</p>
                <p><strong>Slow:</strong> 20 - 30</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 ADX Threshold</h4>
                <p><strong>Range:</strong> 20 - 35</p>
                <p><strong>Default:</strong> 25</p>
                <p><strong>Impact:</strong> MOYEN</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phase 2: SL/TP
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['sltp'] = st.checkbox(
        "", value=st.session_state.progress['sltp'], key="cb2"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['sltp'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['sltp'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">2</span>
            SL/TP & RISK MANAGEMENT
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 SL ATR Multiplier</h4>
                <p><strong>Range:</strong> 1.0 - 4.0</p>
                <p><strong>Default:</strong> 2.5</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 TP Risk:Reward</h4>
                <p><strong>Range:</strong> 1.5 - 5.0</p>
                <p><strong>Default:</strong> 3.0</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 Trailing Start</h4>
                <p><strong>Range:</strong> 0.3 - 1.0</p>
                <p><strong>Default:</strong> 0.5</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phase 3: Volatilite
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['volatilite'] = st.checkbox(
        "", value=st.session_state.progress['volatilite'], key="cb3"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['volatilite'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['volatilite'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">3</span>
            FILTRES DE VOLATILITE
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 ATR Percentile</h4>
                <p><strong>Min:</strong> 10 - 30</p>
                <p><strong>Max:</strong> 70 - 95</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 BB Width Range</h4>
                <p><strong>Min:</strong> 0.005 - 0.02</p>
                <p><strong>Max:</strong> 0.05 - 0.15</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 Historical Vol</h4>
                <p><strong>Min:</strong> 5% - 15%</p>
                <p><strong>Max:</strong> 40% - 80%</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phase 4: Features
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['features'] = st.checkbox(
        "", value=st.session_state.progress['features'], key="cb4"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['features'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['features'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">4</span>
            SELECTION DE FEATURES
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 Nombre Features</h4>
                <p><strong>Range:</strong> 30 - 150</p>
                <p><strong>Default:</strong> 100</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 Scaler Type</h4>
                <p><strong>Options:</strong> Standard/Robust/MinMax</p>
                <p><strong>Rec:</strong> RobustScaler</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 Clip Outliers</h4>
                <p><strong>Range:</strong> 2.0 - 5.0</p>
                <p><strong>Default:</strong> 3.0</p>
                <p><strong>Impact:</strong> MOYEN</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phase 5: Temporels
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['temporels'] = st.checkbox(
        "", value=st.session_state.progress['temporels'], key="cb5"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['temporels'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['temporels'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">5</span>
            FILTRES TEMPORELS
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 Sessions Trading</h4>
                <p><strong>Options:</strong> London/NY/Overlap</p>
                <p><strong>Rec:</strong> LDN + Overlap</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 News Buffer</h4>
                <p><strong>Avant:</strong> 5 - 60 min</p>
                <p><strong>Apres:</strong> 5 - 60 min</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 Friday Close</h4>
                <p><strong>Eviter:</strong> 2 - 6h avant</p>
                <p><strong>Default:</strong> 4h</p>
                <p><strong>Impact:</strong> MOYEN</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phase 6: Rewards
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['rewards'] = st.checkbox(
        "", value=st.session_state.progress['rewards'], key="cb6"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['rewards'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['rewards'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">6</span>
            FONCTION DE REWARD ⚠️
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 Profit Weight</h4>
                <p><strong>Range:</strong> 0.3 - 0.6</p>
                <p><strong>Default:</strong> 0.40</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 Sharpe Weight</h4>
                <p><strong>Range:</strong> 0.1 - 0.3</p>
                <p><strong>Default:</strong> 0.20</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 FTMO Penalty</h4>
                <p><strong>Range:</strong> -5.0 to -1.0</p>
                <p><strong>Default:</strong> -2.0</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phase 7: Architecture
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['architecture'] = st.checkbox(
        "", value=st.session_state.progress['architecture'], key="cb7"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['architecture'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['architecture'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">7</span>
            ARCHITECTURE RESEAU
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 Network Size</h4>
                <p><strong>Options:</strong> small/medium/large</p>
                <p><strong>Rec:</strong> [256, 256]</p>
                <p><strong>Impact:</strong> ELEVE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 Activation</h4>
                <p><strong>Options:</strong> ReLU/Tanh/LeakyReLU</p>
                <p><strong>Rec:</strong> ReLU</p>
                <p><strong>Impact:</strong> MOYEN</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 Dropout</h4>
                <p><strong>Range:</strong> 0.0 - 0.5</p>
                <p><strong>Default:</strong> 0.0</p>
                <p><strong>Impact:</strong> MOYEN</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Phase 8: RL Params
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['rl_params'] = st.checkbox(
        "", value=st.session_state.progress['rl_params'], key="cb8"
    )
with col_content:
    status = "phase-card-done" if st.session_state.progress['rl_params'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['rl_params'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">8</span>
            HYPERPARAMETRES RL
            {status_text}
        </div>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥇 #1 Learning Rate</h4>
                <p><strong>Range:</strong> 1e-6 to 1e-3</p>
                <p><strong>Default:</strong> 1e-4</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥈 #2 Gamma</h4>
                <p><strong>Range:</strong> 0.9 - 0.999</p>
                <p><strong>Default:</strong> 0.99</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
            <div class="top3-box" style="flex: 1; min-width: 200px;">
                <h4>🥉 #3 Entropy Coef</h4>
                <p><strong>Start:</strong> 0.1 - 0.5</p>
                <p><strong>End:</strong> 0.01 - 0.1</p>
                <p><strong>Impact:</strong> CRITIQUE</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")

remaining = 8 - completed
if remaining > 0:
    st.info(f"📊 **{remaining} phases restantes** - Temps estime: ~{remaining * 6}h")
else:
    st.success("🚀 **PRET POUR TRAINING FINAL** - Lance 1.5M steps!")

st.markdown("""
<div style="text-align: center; padding: 30px; color: #666;">
    <p><strong>Guide Optuna Complet - Trading RL Gold</strong></p>
    <p>Version 2.0 PRO - Decembre 2025</p>
    <p>Niveau Institutionnel | 150+ Parametres | 8 Categories</p>
</div>
""", unsafe_allow_html=True)
