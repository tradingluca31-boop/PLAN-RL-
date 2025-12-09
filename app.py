"""
GUIDE OPTUNA COMPLET - Trading RL Gold
Version PRO avec design moderne, checkboxes et details par categorie
"""

import streamlit as st
import pandas as pd

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

# CSS
st.markdown("""
<style>
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
    }
    .main-header p {
        color: #e8e8e8;
        font-size: 1.3rem;
    }
    .phase-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f5);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 2px solid #e0e0e0;
    }
    .phase-card-done {
        background: linear-gradient(145deg, #e8f5e9, #c8e6c9);
        border: 2px solid #4caf50;
    }
    .phase-card-pending {
        background: linear-gradient(145deg, #fff3e0, #ffe0b2);
        border: 2px solid #ff9800;
    }
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
    .progress-container {
        background: #e0e0e0;
        border-radius: 25px;
        height: 40px;
        margin: 20px 0;
        overflow: hidden;
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
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffd700;
    }
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    .status-done {
        background: linear-gradient(135deg, #4caf50, #8bc34a);
        color: white;
        padding: 8px 20px;
        border-radius: 25px;
        font-weight: 700;
    }
    .status-pending {
        background: linear-gradient(135deg, #ff9800, #ffc107);
        color: #1a1a2e;
        padding: 8px 20px;
        border-radius: 25px;
        font-weight: 700;
    }
    .category-header {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        margin: 10px 0;
        font-weight: 600;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
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
progress_pct = int((completed / 8) * 100)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="metric-card"><div class="metric-value">150+</div><div class="metric-label">Parametres</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><div class="metric-value">8</div><div class="metric-label">Categories</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-card"><div class="metric-value">{completed}/8</div><div class="metric-label">Phases Terminees</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="metric-card"><div class="metric-value">~48h</div><div class="metric-label">Temps Total</div></div>', unsafe_allow_html=True)

st.markdown(f'<div class="progress-container"><div class="progress-bar" style="width: {max(progress_pct, 5)}%;">{progress_pct}% Complete</div></div>', unsafe_allow_html=True)

if completed == 8:
    st.balloons()
    st.success("🎉 **TOUTES LES PHASES TERMINEES!** Pret pour le TRAINING FINAL (1.5M steps)")

st.markdown("---")
st.markdown("## 📋 PHASES D'OPTIMISATION")

# ============================================================================
# PHASE 1: INDICATEURS
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['indicateurs'] = st.checkbox("", value=st.session_state.progress['indicateurs'], key="cb1")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - INDICATEURS", expanded=False):
        st.markdown('<div class="category-header">🔹 RSI (Relative Strength Index)</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["rsi_period", "rsi_oversold", "rsi_overbought"],
            "Range": ["5 - 30", "15 - 35", "65 - 85"],
            "Default": [14, 30, 70],
            "Impact": ["🔴 ELEVE", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 MACD</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["macd_fast", "macd_slow", "macd_signal"],
            "Range": ["8 - 15", "20 - 30", "7 - 12"],
            "Default": [12, 26, 9],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Bollinger Bands</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["bb_period", "bb_std"],
            "Range": ["10 - 30", "1.5 - 3.0"],
            "Default": [20, 2.0],
            "Impact": ["🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 ATR & ADX</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["atr_period", "adx_period", "adx_threshold"],
            "Range": ["7 - 21", "10 - 20", "20 - 35"],
            "Default": [14, 14, 25],
            "Impact": ["🟡 MOYEN", "🟡 MOYEN", "🔴 ELEVE"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Stochastic & MAs</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["stoch_k", "stoch_d", "sma_fast", "sma_slow", "ema_fast", "ema_slow"],
            "Range": ["5 - 21", "3 - 7", "5 - 20", "20 - 100", "5 - 15", "20 - 50"],
            "Default": [14, 3, 10, 50, 8, 21],
            "Impact": ["🟢 BAS", "🟢 BAS", "🟢 BAS", "🟢 BAS", "🟢 BAS", "🟢 BAS"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 2: SL/TP
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['sltp'] = st.checkbox("", value=st.session_state.progress['sltp'], key="cb2")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - SL/TP", expanded=False):
        st.markdown('<div class="category-header">🔹 Stop Loss</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["sl_atr_mult", "sl_fixed_pips", "sl_percent", "use_trailing_sl", "trailing_start", "trailing_step"],
            "Range": ["1.0 - 4.0", "50 - 300", "0.5% - 3.0%", "True/False", "0.3 - 1.0", "0.1 - 0.5"],
            "Default": [2.5, 150, "1%", True, 0.5, 0.2],
            "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🔴 ELEVE", "🟢 BAS"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Take Profit</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["tp_rr_ratio", "tp_atr_mult", "use_partial_tp", "partial_tp_1", "partial_tp_2"],
            "Range": ["1.5 - 5.0", "2.0 - 8.0", "True/False", "0.3 - 0.5", "0.5 - 0.7"],
            "Default": [3.0, 4.0, True, 0.33, 0.50],
            "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN", "🟢 BAS", "🟢 BAS"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Break Even & Risk</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["use_break_even", "be_trigger", "be_offset", "risk_per_trade", "max_drawdown"],
            "Range": ["True/False", "0.5 - 1.5", "0 - 20", "0.5% - 2.0%", "5% - 10%"],
            "Default": [True, 1.0, 5, "1%", "8%"],
            "Impact": ["🟡 MOYEN", "🟢 BAS", "🟢 BAS", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 3: VOLATILITE
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['volatilite'] = st.checkbox("", value=st.session_state.progress['volatilite'], key="cb3")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - VOLATILITE", expanded=False):
        st.markdown('<div class="category-header">🔹 ATR Filter</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["atr_filter_min", "atr_filter_max", "atr_percentile_min", "atr_percentile_max"],
            "Range": ["5 - 20", "50 - 150", "10 - 30", "70 - 95"],
            "Default": [10, 100, 20, 90],
            "Impact": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 CRITIQUE"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Bollinger Band Width</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["bb_width_min", "bb_width_max", "bb_squeeze_threshold"],
            "Range": ["0.005 - 0.02", "0.05 - 0.15", "0.01 - 0.03"],
            "Default": [0.01, 0.08, 0.015],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Historical Volatility & Regime</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["hvol_period", "hvol_min", "hvol_max", "trend_threshold", "volatile_threshold"],
            "Range": ["10 - 30", "0.05 - 0.15", "0.40 - 0.80", "0.1 - 0.4", "1.5 - 3.0"],
            "Default": [20, 0.10, 0.60, 0.2, 2.0],
            "Impact": ["🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 4: FEATURES
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['features'] = st.checkbox("", value=st.session_state.progress['features'], key="cb4")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - FEATURES", expanded=False):
        st.markdown('<div class="category-header">🔹 Nombre de Features</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["n_features", "n_price_features", "n_volume_features", "n_technical_features", "n_macro_features"],
            "Range": ["30 - 150", "5 - 20", "2 - 10", "15 - 50", "3 - 15"],
            "Default": [100, 10, 5, 30, 8],
            "Impact": ["🔴 ELEVE", "🟡 MOYEN", "🟢 BAS", "🟡 MOYEN", "🟢 BAS"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Categories de Features</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["use_momentum", "use_trend", "use_volatility", "use_volume", "use_cot", "use_macro", "use_seasonality", "use_correlations"],
            "Options": ["True/False"] * 8,
            "Recommande": [True, True, True, True, True, True, True, True],
            "Impact": ["🟡 MOYEN"] * 8
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Normalisation</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["scaler_type", "zscore_window", "clip_outliers"],
            "Options": ["Standard/Robust/MinMax", "20 - 100", "2.0 - 5.0"],
            "Recommande": ["RobustScaler", 50, 3.0],
            "Impact": ["🔴 ELEVE", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 5: TEMPORELS
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['temporels'] = st.checkbox("", value=st.session_state.progress['temporels'], key="cb5")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - TEMPORELS", expanded=False):
        st.markdown('<div class="category-header">🔹 Sessions de Trading</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["trade_london", "trade_ny", "trade_asia", "trade_overlap", "london_start", "london_end", "ny_start", "ny_end"],
            "Range": ["T/F", "T/F", "T/F", "T/F", "7 - 9", "15 - 17", "12 - 14", "20 - 22"],
            "Recommande": [True, True, False, True, 8, 16, 13, 21],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🟢 BAS", "🔴 ELEVE", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Filtres Jours</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["trade_monday", "trade_tuesday", "trade_wednesday", "trade_thursday", "trade_friday", "avoid_friday_close"],
            "Range": ["T/F", "T/F", "T/F", "T/F", "T/F", "2 - 6h"],
            "Recommande": [True, True, True, True, True, "4h"],
            "Impact": ["🟢 BAS", "🟢 BAS", "🟢 BAS", "🟢 BAS", "🟢 BAS", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Filtres News</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["avoid_high_impact", "news_buffer_before", "news_buffer_after", "avoid_fomc", "avoid_nfp"],
            "Range": ["T/F", "5 - 60 min", "5 - 60 min", "T/F", "T/F"],
            "Recommande": [True, "30 min", "15 min", True, True],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 6: REWARDS
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['rewards'] = st.checkbox("", value=st.session_state.progress['rewards'], key="cb6")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - REWARDS", expanded=False):
        st.warning("⚠️ La fonction de reward est CRITIQUE. Un mauvais reward = agent qui apprend mal!")

        st.markdown('<div class="category-header">🔹 Poids Principaux</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["reward_profit_weight", "reward_sharpe_weight", "reward_dd_weight", "reward_trade_weight"],
            "Range": ["0.3 - 0.6", "0.1 - 0.3", "0.05 - 0.20", "0.05 - 0.15"],
            "Default": [0.40, 0.20, 0.10, 0.10],
            "Impact": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 ELEVE", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Bonus et Penalites</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["bonus_win", "penalty_loss", "bonus_4r_plus", "bonus_quick_cut", "penalty_hold_too_long"],
            "Range": ["0.01 - 0.10", "-0.15 to -0.05", "0.10 - 0.30", "0.01 - 0.05", "-0.05 to -0.01"],
            "Default": [0.05, -0.10, 0.20, 0.03, -0.02],
            "Impact": ["🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🟢 BAS"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Risk & Shaping</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["penalty_ftmo_breach", "penalty_daily_breach", "reward_risk_adjusted", "direction_bonus", "diversity_penalty"],
            "Range": ["-5.0 to -1.0", "-2.0 to -0.5", "0.01 - 0.05", "0.01 - 0.05", "-0.10 to -0.01"],
            "Default": [-2.0, -1.0, 0.02, 0.02, -0.05],
            "Impact": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 7: ARCHITECTURE
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['architecture'] = st.checkbox("", value=st.session_state.progress['architecture'], key="cb7")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - ARCHITECTURE", expanded=False):
        st.markdown('<div class="category-header">🔹 Structure du Reseau</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["n_layers", "layer_size", "net_arch_pattern"],
            "Options": ["2 - 4", "64 - 1024", "small/medium/large/deep/pyramid"],
            "Recommande": [2, 256, "medium [256,256]"],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🔴 ELEVE"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Activation & Regularisation</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["activation", "dropout", "use_batch_norm", "use_layer_norm", "weight_decay"],
            "Options": ["ReLU/Tanh/LeakyReLU/ELU", "0.0 - 0.5", "T/F", "T/F", "0.0 - 0.01"],
            "Recommande": ["ReLU", 0.0, False, False, 0.0],
            "Impact": ["🟡 MOYEN", "🟡 MOYEN", "🟢 BAS", "🟢 BAS", "🟢 BAS"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Architectures Predefinies</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Pattern": ["small", "medium", "large", "deep", "pyramid"],
            "Architecture": ["[64, 64]", "[256, 256]", "[512, 512]", "[256, 256, 256]", "[512, 256, 128]"],
            "Usage": ["Rapide, risque underfitting", "RECOMMANDE - Equilibre", "Plus de capacite", "3 couches profondes", "Reduction progressive"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 8: RL PARAMS
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['rl_params'] = st.checkbox("", value=st.session_state.progress['rl_params'], key="cb8")
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
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - RL", expanded=False):
        tab_ppo, tab_sac, tab_td3, tab_a2c = st.tabs(["PPO (Agent 7)", "SAC (Agent 8)", "TD3 (Agent 9)", "A2C (Agent 11)"])

        with tab_ppo:
            st.markdown('<div class="category-header">🔹 PPO - Proximal Policy Optimization</div>', unsafe_allow_html=True)
            st.dataframe(pd.DataFrame({
                "Parametre": ["learning_rate", "n_steps", "batch_size", "n_epochs", "gamma", "gae_lambda", "clip_range", "ent_coef_start", "ent_coef_end", "vf_coef", "max_grad_norm"],
                "Range": ["1e-6 to 1e-3", "512 - 4096", "32 - 256", "5 - 20", "0.9 - 0.999", "0.9 - 0.99", "0.1 - 0.3", "0.1 - 0.5", "0.01 - 0.1", "0.3 - 0.7", "0.3 - 1.0"],
                "Default": ["1e-4", 2048, 64, 10, 0.99, 0.95, 0.2, 0.20, 0.05, 0.5, 0.5],
                "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN", "🟢 BAS", "🔴 CRITIQUE", "🟢 BAS", "🟢 BAS", "🔴 CRITIQUE", "🔴 ELEVE", "🟢 BAS", "🟢 BAS"]
            }), use_container_width=True, hide_index=True)

        with tab_sac:
            st.markdown('<div class="category-header">🔹 SAC - Soft Actor-Critic</div>', unsafe_allow_html=True)
            st.dataframe(pd.DataFrame({
                "Parametre": ["learning_rate", "buffer_size", "batch_size", "tau", "gamma", "learning_starts", "train_freq", "gradient_steps"],
                "Range": ["1e-5 to 1e-3", "50K - 500K", "128 - 512", "0.001 - 0.02", "0.95 - 0.999", "1K - 20K", "1 - 8", "1 - 4"],
                "Default": ["3e-4", "100K", 256, 0.005, 0.99, "10K", 1, 1],
                "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN", "🟢 BAS", "🔴 CRITIQUE", "🟡 MOYEN", "🟢 BAS", "🟢 BAS"]
            }), use_container_width=True, hide_index=True)

        with tab_td3:
            st.markdown('<div class="category-header">🔹 TD3 - Twin Delayed DDPG</div>', unsafe_allow_html=True)
            st.dataframe(pd.DataFrame({
                "Parametre": ["learning_rate", "buffer_size", "batch_size", "tau", "gamma", "policy_delay", "target_policy_noise", "target_noise_clip"],
                "Range": ["1e-5 to 1e-3", "50K - 500K", "128 - 512", "0.001 - 0.02", "0.95 - 0.999", "1 - 4", "0.1 - 0.3", "0.3 - 0.7"],
                "Default": ["3e-4", "100K", 256, 0.005, 0.99, 2, 0.2, 0.5],
                "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN", "🟢 BAS", "🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN", "🟢 BAS"]
            }), use_container_width=True, hide_index=True)

        with tab_a2c:
            st.markdown('<div class="category-header">🔹 A2C - Advantage Actor-Critic</div>', unsafe_allow_html=True)
            st.dataframe(pd.DataFrame({
                "Parametre": ["learning_rate", "n_steps", "gamma", "gae_lambda", "ent_coef", "vf_coef", "max_grad_norm"],
                "Range": ["1e-5 to 1e-2", "3 - 20", "0.95 - 0.999", "0.9 - 0.99", "0.0 - 0.2", "0.3 - 0.7", "0.3 - 1.0"],
                "Default": ["7e-4", 5, 0.99, 0.95, 0.01, 0.5, 0.5],
                "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🔴 CRITIQUE", "🟢 BAS", "🟡 MOYEN", "🟢 BAS", "🟢 BAS"]
            }), use_container_width=True, hide_index=True)

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
    <p>Version 3.0 PRO - Decembre 2025</p>
</div>
""", unsafe_allow_html=True)
