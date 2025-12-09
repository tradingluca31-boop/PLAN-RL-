"""
GUIDE OPTUNA COMPLET - Trading RL Gold
Dashboard Streamlit pour visualiser le plan d'optimisation
Avec suivi d'avancement et TOP 3 parametres
"""

import streamlit as st

st.set_page_config(
    page_title="Guide Optuna - RL Trading Gold",
    page_icon="🏆",
    layout="wide"
)

# Initialize session state for checkboxes
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
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    .top3-box {
        background: linear-gradient(135deg, #ffd700, #ffaa00);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .top3-title {
        color: #1a1a2e;
        font-weight: bold;
        font-size: 1.1em;
    }
    .progress-done {
        background: #00c853;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
    }
    .progress-pending {
        background: #ff6b00;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🏆 GUIDE OPTUNA COMPLET</h1><p>Optimisation Professionnelle pour Agent RL Trading Gold</p></div>', unsafe_allow_html=True)

# ============================================================================
# SIDEBAR - SUIVI D'AVANCEMENT
# ============================================================================
st.sidebar.header("📋 SUIVI D'AVANCEMENT")
st.sidebar.markdown("---")

# Checkboxes pour chaque phase
st.sidebar.subheader("Cochez quand termine:")

st.session_state.progress['indicateurs'] = st.sidebar.checkbox(
    "1. Indicateurs Techniques",
    value=st.session_state.progress['indicateurs'],
    key='cb_ind'
)
st.session_state.progress['sltp'] = st.sidebar.checkbox(
    "2. SL/TP & Risk Management",
    value=st.session_state.progress['sltp'],
    key='cb_sltp'
)
st.session_state.progress['volatilite'] = st.sidebar.checkbox(
    "3. Filtres Volatilite",
    value=st.session_state.progress['volatilite'],
    key='cb_vol'
)
st.session_state.progress['features'] = st.sidebar.checkbox(
    "4. Selection Features",
    value=st.session_state.progress['features'],
    key='cb_feat'
)
st.session_state.progress['temporels'] = st.sidebar.checkbox(
    "5. Filtres Temporels",
    value=st.session_state.progress['temporels'],
    key='cb_temp'
)
st.session_state.progress['rewards'] = st.sidebar.checkbox(
    "6. Fonction de Reward",
    value=st.session_state.progress['rewards'],
    key='cb_rew'
)
st.session_state.progress['architecture'] = st.sidebar.checkbox(
    "7. Architecture Reseau",
    value=st.session_state.progress['architecture'],
    key='cb_arch'
)
st.session_state.progress['rl_params'] = st.sidebar.checkbox(
    "8. Hyperparametres RL",
    value=st.session_state.progress['rl_params'],
    key='cb_rl'
)

# Progress bar
completed = sum(st.session_state.progress.values())
total = len(st.session_state.progress)
progress_pct = completed / total

st.sidebar.markdown("---")
st.sidebar.subheader(f"Progression: {completed}/{total}")
st.sidebar.progress(progress_pct)

if progress_pct == 1.0:
    st.sidebar.success("🎉 TOUTES LES PHASES TERMINEES!")
    st.sidebar.info("👉 Pret pour TRAINING FINAL (1.5M steps)")

st.sidebar.markdown("---")
st.sidebar.caption("Temps estime: 6h par phase")
st.sidebar.caption("Total: ~48 heures")

# ============================================================================
# METRICS
# ============================================================================
col1, col2, col3, col4 = st.columns(4)
col1.metric("Parametres", "150+")
col2.metric("Categories", "8")
col3.metric("Phases Terminees", f"{completed}/8")
col4.metric("Trials/Phase", "100")

st.divider()

# ============================================================================
# TOP 3 PARAMETRES PAR CATEGORIE
# ============================================================================
st.header("🏅 TOP 3 PARAMETRES LES PLUS IMPORTANTS")
st.caption("Les parametres qui ont le plus d'impact sur la performance")

top3_col1, top3_col2, top3_col3, top3_col4 = st.columns(4)

with top3_col1:
    st.subheader("1. Indicateurs")
    status = "✅" if st.session_state.progress['indicateurs'] else "⏳"
    st.markdown(f"""
    {status} **RSI Period**: 5-30 (def: 14)

    {status} **MACD Fast/Slow**: 8-15 / 20-30

    {status} **ADX Threshold**: 20-35
    """)

with top3_col2:
    st.subheader("2. SL/TP")
    status = "✅" if st.session_state.progress['sltp'] else "⏳"
    st.markdown(f"""
    {status} **SL ATR Mult**: 1.0-4.0 (def: 2.5)

    {status} **TP R:R Ratio**: 1.5-5.0 (def: 3.0)

    {status} **Trailing Start**: 0.3-1.0
    """)

with top3_col3:
    st.subheader("3. Volatilite")
    status = "✅" if st.session_state.progress['volatilite'] else "⏳"
    st.markdown(f"""
    {status} **ATR Percentile**: 10-95

    {status} **BB Width**: 0.005-0.15

    {status} **HVol Range**: 5%-80%
    """)

with top3_col4:
    st.subheader("4. Features")
    status = "✅" if st.session_state.progress['features'] else "⏳"
    st.markdown(f"""
    {status} **N Features**: 30-150

    {status} **Scaler**: RobustScaler

    {status} **Clip Outliers**: 2.0-5.0
    """)

top3_col5, top3_col6, top3_col7, top3_col8 = st.columns(4)

with top3_col5:
    st.subheader("5. Temporels")
    status = "✅" if st.session_state.progress['temporels'] else "⏳"
    st.markdown(f"""
    {status} **Sessions**: LDN/NY/Overlap

    {status} **News Buffer**: 5-60 min

    {status} **Friday Close**: 2-6h avant
    """)

with top3_col6:
    st.subheader("6. Rewards")
    status = "✅" if st.session_state.progress['rewards'] else "⏳"
    st.markdown(f"""
    {status} **Profit Weight**: 0.3-0.6

    {status} **Sharpe Weight**: 0.1-0.3

    {status} **FTMO Penalty**: -5.0 to -1.0
    """)

with top3_col7:
    st.subheader("7. Architecture")
    status = "✅" if st.session_state.progress['architecture'] else "⏳"
    st.markdown(f"""
    {status} **Net Arch**: [256,256] rec.

    {status} **Activation**: ReLU/Tanh

    {status} **Dropout**: 0.0-0.3
    """)

with top3_col8:
    st.subheader("8. RL Params")
    status = "✅" if st.session_state.progress['rl_params'] else "⏳"
    st.markdown(f"""
    {status} **Learning Rate**: 1e-6 to 1e-3

    {status} **Gamma**: 0.9-0.999

    {status} **Entropy**: 0.1-0.5 start
    """)

st.divider()

# ============================================================================
# TABS - DETAILS COMPLETS
# ============================================================================
st.header("📊 DETAILS PAR CATEGORIE")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "1. Indicateurs",
    "2. SL/TP",
    "3. Volatilite",
    "4. Features",
    "5. Temporels",
    "6. Rewards",
    "7. Architecture",
    "8. RL Params"
])

with tab1:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['indicateurs']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("Indicateurs Techniques")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 RSI Period**\n\nRange: 5-30\n\nDefault: 14\n\nImpact: ELEVE")
    with top_col2:
        st.info("**#2 MACD Fast/Slow**\n\nFast: 8-15, Slow: 20-30\n\nDefault: 12/26\n\nImpact: ELEVE")
    with top_col3:
        st.info("**#3 ADX Threshold**\n\nRange: 20-35\n\nDefault: 25\n\nImpact: MOYEN-ELEVE")

    st.subheader("Tous les parametres")
    st.dataframe({
        "Parametre": ["rsi_period", "rsi_oversold", "rsi_overbought", "macd_fast", "macd_slow", "macd_signal", "bb_period", "bb_std", "atr_period", "adx_period", "adx_threshold", "stoch_k", "sma_fast", "sma_slow"],
        "Range": ["5-30", "15-35", "65-85", "8-15", "20-30", "7-12", "10-30", "1.5-3.0", "7-21", "10-20", "20-35", "5-21", "5-20", "20-100"],
        "Default": [14, 30, 70, 12, 26, 9, 20, 2.0, 14, 14, 25, 14, 10, 50],
        "Priorite": ["🔴 HAUTE", "🟡 MOYENNE", "🟡 MOYENNE", "🔴 HAUTE", "🔴 HAUTE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🔴 HAUTE", "🟢 BASSE", "🟢 BASSE", "🟢 BASSE"]
    }, use_container_width=True)

    st.code("""
# Code Optuna pour indicateurs
rsi_period = trial.suggest_int("rsi_period", 5, 30)
macd_fast = trial.suggest_int("macd_fast", 8, 15)
macd_slow = trial.suggest_int("macd_slow", 20, 30)
adx_threshold = trial.suggest_int("adx_threshold", 20, 35)
    """, language="python")

with tab2:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['sltp']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("SL/TP & Risk Management")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 SL ATR Multiplier**\n\nRange: 1.0-4.0\n\nDefault: 2.5\n\nImpact: CRITIQUE")
    with top_col2:
        st.info("**#2 TP Risk:Reward**\n\nRange: 1.5-5.0\n\nDefault: 3.0\n\nImpact: CRITIQUE")
    with top_col3:
        st.info("**#3 Trailing Start**\n\nRange: 0.3-1.0\n\nDefault: 0.5\n\nImpact: ELEVE")

    st.dataframe({
        "Parametre": ["sl_atr_mult", "tp_rr_ratio", "trailing_start", "use_trailing_sl", "use_partial_tp", "use_break_even", "be_trigger", "risk_per_trade", "max_drawdown"],
        "Range": ["1.0-4.0", "1.5-5.0", "0.3-1.0", "T/F", "T/F", "T/F", "0.5-1.5", "0.5-2.0%", "5-10%"],
        "Default": [2.5, 3.0, 0.5, True, True, True, 1.0, "1%", "8%"],
        "Priorite": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 HAUTE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🟢 BASSE", "🟡 MOYENNE", "🟡 MOYENNE"]
    }, use_container_width=True)

with tab3:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['volatilite']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("Filtres de Volatilite")

    st.warning("Les filtres de volatilite peuvent ameliorer le Sharpe de +30%!")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 ATR Percentile**\n\nMin: 10-30, Max: 70-95\n\nImpact: CRITIQUE")
    with top_col2:
        st.info("**#2 BB Width Range**\n\nMin: 0.005-0.02\nMax: 0.05-0.15\n\nImpact: ELEVE")
    with top_col3:
        st.info("**#3 Historical Vol**\n\nMin: 5-15%\nMax: 40-80%\n\nImpact: ELEVE")

    st.dataframe({
        "Parametre": ["atr_percentile_min", "atr_percentile_max", "bb_width_min", "bb_width_max", "hvol_min", "hvol_max", "trend_threshold", "volatile_threshold"],
        "Range": ["10-30", "70-95", "0.005-0.02", "0.05-0.15", "0.05-0.15", "0.40-0.80", "0.1-0.4", "1.5-3.0"],
        "Priorite": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 HAUTE", "🔴 HAUTE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE"]
    }, use_container_width=True)

with tab4:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['features']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("Selection de Features")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 Nombre Features**\n\nRange: 30-150\n\nDefault: 100\n\nImpact: ELEVE")
    with top_col2:
        st.info("**#2 Scaler Type**\n\nOptions: Standard, Robust, MinMax\n\nRec: RobustScaler\n\nImpact: ELEVE")
    with top_col3:
        st.info("**#3 Clip Outliers**\n\nRange: 2.0-5.0\n\nDefault: 3.0\n\nImpact: MOYEN")

    st.dataframe({
        "Parametre": ["n_features", "scaler_type", "clip_outliers", "use_momentum", "use_trend", "use_volatility", "use_cot", "use_macro"],
        "Range/Options": ["30-150", "Standard/Robust/MinMax", "2.0-5.0", "T/F", "T/F", "T/F", "T/F", "T/F"],
        "Recommande": [100, "RobustScaler", 3.0, True, True, True, True, True],
        "Priorite": ["🔴 HAUTE", "🔴 HAUTE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🟢 BASSE", "🟢 BASSE"]
    }, use_container_width=True)

with tab5:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['temporels']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("Filtres Temporels")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 Sessions Trading**\n\nLondon/NY/Overlap\n\nRec: LDN + Overlap\n\nImpact: ELEVE")
    with top_col2:
        st.info("**#2 News Buffer**\n\nAvant: 5-60min\nApres: 5-60min\n\nImpact: ELEVE")
    with top_col3:
        st.info("**#3 Friday Close**\n\nEviter: 2-6h avant\n\nDefault: 4h\n\nImpact: MOYEN")

    st.dataframe({
        "Parametre": ["trade_london", "trade_ny", "trade_overlap", "news_buffer_before", "news_buffer_after", "avoid_friday_close", "trade_monday", "trade_friday"],
        "Range": ["T/F", "T/F", "T/F", "5-60min", "5-60min", "2-6h", "T/F", "T/F"],
        "Recommande": [True, True, True, "30min", "15min", "4h", True, True],
        "Priorite": ["🔴 HAUTE", "🔴 HAUTE", "🔴 HAUTE", "🔴 HAUTE", "🟡 MOYENNE", "🟡 MOYENNE", "🟢 BASSE", "🟢 BASSE"]
    }, use_container_width=True)

with tab6:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['rewards']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("Fonction de Reward")

    st.error("⚠️ ATTENTION: La reward function est CRITIQUE. Un mauvais reward = agent qui apprend mal!")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 Profit Weight**\n\nRange: 0.3-0.6\n\nDefault: 0.40\n\nImpact: CRITIQUE")
    with top_col2:
        st.info("**#2 Sharpe Weight**\n\nRange: 0.1-0.3\n\nDefault: 0.20\n\nImpact: CRITIQUE")
    with top_col3:
        st.info("**#3 FTMO Penalty**\n\nRange: -5.0 to -1.0\n\nDefault: -2.0\n\nImpact: CRITIQUE")

    st.dataframe({
        "Parametre": ["reward_profit_weight", "reward_sharpe_weight", "reward_dd_weight", "penalty_ftmo_breach", "bonus_win", "penalty_loss", "bonus_4r_plus", "diversity_penalty"],
        "Range": ["0.3-0.6", "0.1-0.3", "0.05-0.20", "-5.0 to -1.0", "0.01-0.10", "-0.15 to -0.05", "0.10-0.30", "-0.10 to -0.01"],
        "Default": [0.40, 0.20, 0.10, -2.0, 0.05, -0.10, 0.20, -0.05],
        "Priorite": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 HAUTE", "🔴 CRITIQUE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE", "🟡 MOYENNE"]
    }, use_container_width=True)

with tab7:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['architecture']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("Architecture Reseau")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 Network Size**\n\nOptions: small/medium/large\n\nRec: [256,256]\n\nImpact: ELEVE")
    with top_col2:
        st.info("**#2 Activation**\n\nOptions: ReLU/Tanh/LeakyReLU\n\nRec: ReLU\n\nImpact: MOYEN")
    with top_col3:
        st.info("**#3 Dropout**\n\nRange: 0.0-0.5\n\nDefault: 0.0\n\nImpact: MOYEN")

    st.subheader("Architectures Predefinies")
    st.dataframe({
        "Pattern": ["small", "medium", "large", "deep", "pyramid"],
        "Architecture": ["[64, 64]", "[256, 256]", "[512, 512]", "[256, 256, 256]", "[512, 256, 128]"],
        "Usage": ["Rapide", "RECOMMANDE", "Plus capacite", "3 couches", "Progressif"],
        "Priorite": ["🟢", "🔴 RECOMMANDE", "🟡", "🟡", "🟢"]
    }, use_container_width=True)

with tab8:
    col_status, col_title = st.columns([1, 10])
    with col_status:
        if st.session_state.progress['rl_params']:
            st.markdown('<span class="progress-done">FAIT</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="progress-pending">A FAIRE</span>', unsafe_allow_html=True)
    with col_title:
        st.header("Hyperparametres RL")

    st.subheader("🏅 TOP 3 A OPTIMISER EN PRIORITE")
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        st.info("**#1 Learning Rate**\n\nRange: 1e-6 to 1e-3\n\nDefault: 1e-4\n\nImpact: CRITIQUE")
    with top_col2:
        st.info("**#2 Gamma**\n\nRange: 0.9-0.999\n\nDefault: 0.99\n\nImpact: CRITIQUE")
    with top_col3:
        st.info("**#3 Entropy Coef**\n\nStart: 0.1-0.5\nEnd: 0.01-0.1\n\nImpact: CRITIQUE")

    algo_tab1, algo_tab2 = st.tabs(["PPO (Agent 7)", "SAC (Agent 8)"])

    with algo_tab1:
        st.dataframe({
            "Parametre": ["learning_rate", "gamma", "ent_coef_start", "ent_coef_end", "n_steps", "batch_size", "n_epochs", "clip_range", "gae_lambda"],
            "Range": ["1e-6 to 1e-3", "0.9-0.999", "0.1-0.5", "0.01-0.1", "512-4096", "32-256", "5-20", "0.1-0.3", "0.9-0.99"],
            "Default": ["1e-4", 0.99, 0.20, 0.05, 2048, 64, 10, 0.2, 0.95],
            "Priorite": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 CRITIQUE", "🔴 HAUTE", "🟡 MOYENNE", "🟡 MOYENNE", "🟢 BASSE", "🟢 BASSE", "🟢 BASSE"]
        }, use_container_width=True)

    with algo_tab2:
        st.dataframe({
            "Parametre": ["learning_rate", "gamma", "buffer_size", "batch_size", "tau", "learning_starts"],
            "Range": ["1e-5 to 1e-3", "0.95-0.999", "50K-500K", "128-512", "0.001-0.02", "1K-20K"],
            "Default": ["3e-4", 0.99, "100K", 256, 0.005, "10K"],
            "Priorite": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🟡 MOYENNE", "🟡 MOYENNE", "🟢 BASSE", "🟢 BASSE"]
        }, use_container_width=True)

st.divider()

# ============================================================================
# WORKFLOW FINAL
# ============================================================================
st.header("🔄 Workflow Sequentiel")

workflow_data = [
    ("1. Indicateurs", st.session_state.progress['indicateurs'], "6h"),
    ("2. SL/TP", st.session_state.progress['sltp'], "6h"),
    ("3. Volatilite", st.session_state.progress['volatilite'], "6h"),
    ("4. Features", st.session_state.progress['features'], "6h"),
    ("5. Temporels", st.session_state.progress['temporels'], "6h"),
    ("6. Rewards", st.session_state.progress['rewards'], "6h"),
    ("7. Architecture", st.session_state.progress['architecture'], "6h"),
    ("8. RL Params", st.session_state.progress['rl_params'], "6h"),
]

cols = st.columns(8)
for i, (name, done, time) in enumerate(workflow_data):
    with cols[i]:
        if done:
            st.success(f"✅\n\n{name}\n\n{time}")
        else:
            st.warning(f"⏳\n\n{name}\n\n{time}")

if progress_pct == 1.0:
    st.balloons()
    st.success("🎉 **TOUTES LES PHASES TERMINEES!** Tu peux maintenant lancer le TRAINING FINAL (1.5M steps)")
else:
    remaining = 8 - completed
    st.info(f"📊 **{remaining} phases restantes** - Temps estime: ~{remaining * 6}h")

st.divider()

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p><strong>Guide Optuna Complet - Trading RL Gold</strong></p>
    <p>Version 1.0 - Decembre 2025 | Niveau Institutionnel</p>
</div>
""", unsafe_allow_html=True)
