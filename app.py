"""
GUIDE OPTUNA COMPLET - Trading RL Gold
Version 4.0 PRO - ORDRE REVISE (Impact Maximum)
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Guide Optuna - RL Trading Gold",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state - ORDRE REVISE (Impact Maximum)
if 'progress' not in st.session_state:
    st.session_state.progress = {
        'rl_params': False,
        'rewards': False,
        'features': False,
        'architecture': False,
        'indicateurs': False,
        'volatilite': False,
        'temporels': False,
        'sltp': False,
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
    .main-header h1 { color: #ffd700; font-size: 3rem; margin-bottom: 10px; }
    .main-header p { color: #e8e8e8; font-size: 1.3rem; }
    .phase-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f5);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 2px solid #e0e0e0;
    }
    .phase-card-done { background: linear-gradient(145deg, #e8f5e9, #c8e6c9); border: 2px solid #4caf50; }
    .phase-card-pending { background: linear-gradient(145deg, #fff3e0, #ffe0b2); border: 2px solid #ff9800; }
    .phase-title { font-size: 1.8rem; font-weight: 700; margin-bottom: 15px; display: flex; align-items: center; gap: 15px; }
    .phase-number {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white; width: 50px; height: 50px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700;
    }
    .progress-container { background: #e0e0e0; border-radius: 25px; height: 40px; margin: 20px 0; overflow: hidden; }
    .progress-bar {
        background: linear-gradient(90deg, #4caf50, #8bc34a);
        height: 100%; border-radius: 25px;
        display: flex; align-items: center; justify-content: center;
        color: white; font-weight: 700; font-size: 1.1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white; padding: 25px; border-radius: 15px; text-align: center;
    }
    .metric-value { font-size: 2.5rem; font-weight: 700; color: #ffd700; }
    .metric-label { font-size: 1rem; opacity: 0.9; }
    .status-done { background: linear-gradient(135deg, #4caf50, #8bc34a); color: white; padding: 8px 20px; border-radius: 25px; font-weight: 700; }
    .status-pending { background: linear-gradient(135deg, #ff9800, #ffc107); color: #1a1a2e; padding: 8px 20px; border-radius: 25px; font-weight: 700; }
    .category-header { background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 10px 20px; border-radius: 10px; margin: 10px 0; font-weight: 600; }
    .reason-box { background: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px; margin: 10px 0; border-radius: 0 10px 10px 0; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="main-header">
    <h1>🏆 GUIDE OPTUNA COMPLET</h1>
    <p>Optimisation Professionnelle pour Agent RL Trading Gold</p>
    <p style="color: #ffd700; font-weight: 600;">ORDRE REVISE - IMPACT MAXIMUM</p>
</div>
""", unsafe_allow_html=True)

# METRICS
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
st.markdown("## 📋 PHASES D'OPTIMISATION (Ordre Impact Maximum)")

# ============================================================================
# PHASE 1: RL PARAMS (PREMIER - LE PLUS IMPORTANT)
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['rl_params'] = st.checkbox("", value=st.session_state.progress['rl_params'], key="cb1")
with col_content:
    status = "phase-card-done" if st.session_state.progress['rl_params'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['rl_params'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">1</span>
            HYPERPARAMETRES RL 🔥
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en premier?</strong> Si learning_rate ou entropy sont mauvais, l'agent n'apprendra JAMAIS. C'est la base de tout.
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
# PHASE 2: REWARDS
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['rewards'] = st.checkbox("", value=st.session_state.progress['rewards'], key="cb2")
with col_content:
    status = "phase-card-done" if st.session_state.progress['rewards'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['rewards'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">2</span>
            FONCTION DE REWARD ⚠️
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en deuxieme?</strong> La reward definit CE QUE l'agent apprend. Mauvaise reward = agent qui apprend les mauvais comportements.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - REWARDS", expanded=False):
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
            "Parametre": ["penalty_ftmo_breach", "penalty_daily_breach", "direction_bonus", "diversity_penalty"],
            "Range": ["-5.0 to -1.0", "-2.0 to -0.5", "0.01 - 0.05", "-0.10 to -0.01"],
            "Default": [-2.0, -1.0, 0.02, -0.05],
            "Impact": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 3: FEATURES
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['features'] = st.checkbox("", value=st.session_state.progress['features'], key="cb3")
with col_content:
    status = "phase-card-done" if st.session_state.progress['features'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['features'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">3</span>
            SELECTION DE FEATURES
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en troisieme?</strong> Les features sont l'INFORMATION que l'agent voit. Garbage in = Garbage out.
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

        st.markdown('<div class="category-header">🔹 Categories</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["use_momentum", "use_trend", "use_volatility", "use_volume", "use_cot", "use_macro", "use_seasonality"],
            "Options": ["True/False"] * 7,
            "Recommande": [True] * 7,
            "Impact": ["🟡 MOYEN"] * 7
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Normalisation</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["scaler_type", "zscore_window", "clip_outliers"],
            "Options": ["Standard/Robust/MinMax", "20 - 100", "2.0 - 5.0"],
            "Recommande": ["RobustScaler", 50, 3.0],
            "Impact": ["🔴 ELEVE", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 4: ARCHITECTURE
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['architecture'] = st.checkbox("", value=st.session_state.progress['architecture'], key="cb4")
with col_content:
    status = "phase-card-done" if st.session_state.progress['architecture'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['architecture'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">4</span>
            ARCHITECTURE RESEAU
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en quatrieme?</strong> L'architecture determine la CAPACITE du modele a apprendre des patterns complexes.
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

        st.markdown('<div class="category-header">🔹 Architectures Predefinies</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Pattern": ["small", "medium", "large", "deep", "pyramid"],
            "Architecture": ["[64, 64]", "[256, 256]", "[512, 512]", "[256, 256, 256]", "[512, 256, 128]"],
            "Usage": ["Rapide", "RECOMMANDE", "Plus capacite", "3 couches", "Progressif"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 5: INDICATEURS
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['indicateurs'] = st.checkbox("", value=st.session_state.progress['indicateurs'], key="cb5")
with col_content:
    status = "phase-card-done" if st.session_state.progress['indicateurs'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['indicateurs'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">5</span>
            INDICATEURS TECHNIQUES
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en cinquieme?</strong> Fine-tuning des indicateurs - les periodes RSI, MACD etc. Impact moyen sur performance.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - INDICATEURS", expanded=False):
        st.markdown('<div class="category-header">🔹 RSI</div>', unsafe_allow_html=True)
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

        st.markdown('<div class="category-header">🔹 Autres</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["bb_period", "bb_std", "atr_period", "adx_period", "adx_threshold"],
            "Range": ["10-30", "1.5-3.0", "7-21", "10-20", "20-35"],
            "Default": [20, 2.0, 14, 14, 25],
            "Impact": ["🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🟡 MOYEN", "🔴 ELEVE"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 6: VOLATILITE
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['volatilite'] = st.checkbox("", value=st.session_state.progress['volatilite'], key="cb6")
with col_content:
    status = "phase-card-done" if st.session_state.progress['volatilite'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['volatilite'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">6</span>
            FILTRES DE VOLATILITE
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en sixieme?</strong> Filtrer QUAND trader. Eviter les periodes dangereuses (flash crash, news).
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

        st.markdown('<div class="category-header">🔹 BB Width & Historical Vol</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["bb_width_min", "bb_width_max", "hvol_min", "hvol_max"],
            "Range": ["0.005-0.02", "0.05-0.15", "0.05-0.15", "0.40-0.80"],
            "Default": [0.01, 0.08, 0.10, 0.60],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 7: TEMPORELS
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['temporels'] = st.checkbox("", value=st.session_state.progress['temporels'], key="cb7")
with col_content:
    status = "phase-card-done" if st.session_state.progress['temporels'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['temporels'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">7</span>
            FILTRES TEMPORELS
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en septieme?</strong> Sessions (London/NY), jours de la semaine, news buffer.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - TEMPORELS", expanded=False):
        st.markdown('<div class="category-header">🔹 Sessions</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["trade_london", "trade_ny", "trade_overlap", "trade_asia"],
            "Options": ["T/F", "T/F", "T/F", "T/F"],
            "Recommande": [True, True, True, False],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🔴 ELEVE", "🟢 BAS"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 News</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["avoid_high_impact", "news_buffer_before", "news_buffer_after"],
            "Range": ["T/F", "5-60 min", "5-60 min"],
            "Recommande": [True, "30 min", "15 min"],
            "Impact": ["🔴 ELEVE", "🔴 ELEVE", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

# ============================================================================
# PHASE 8: SL/TP
# ============================================================================
col_check, col_content = st.columns([1, 11])
with col_check:
    st.session_state.progress['sltp'] = st.checkbox("", value=st.session_state.progress['sltp'], key="cb8")
with col_content:
    status = "phase-card-done" if st.session_state.progress['sltp'] else "phase-card-pending"
    status_text = '<span class="status-done">✅ TERMINE</span>' if st.session_state.progress['sltp'] else '<span class="status-pending">⏳ A FAIRE</span>'

    st.markdown(f"""
    <div class="phase-card {status}">
        <div class="phase-title">
            <span class="phase-number">8</span>
            SL/TP & RISK MANAGEMENT
            {status_text}
        </div>
        <div class="reason-box">
            <strong>Pourquoi en dernier?</strong> Risk management - fine-tuning final une fois que l'agent trade correctement.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 VOIR TOUS LES PARAMETRES - SL/TP", expanded=False):
        st.markdown('<div class="category-header">🔹 Stop Loss</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["sl_atr_mult", "use_trailing_sl", "trailing_start"],
            "Range": ["1.0 - 4.0", "T/F", "0.3 - 1.0"],
            "Default": [2.5, True, 0.5],
            "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🔴 ELEVE"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Take Profit</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["tp_rr_ratio", "tp_atr_mult", "use_partial_tp"],
            "Range": ["1.5 - 5.0", "2.0 - 8.0", "T/F"],
            "Default": [3.0, 4.0, True],
            "Impact": ["🔴 CRITIQUE", "🟡 MOYEN", "🟡 MOYEN"]
        }), use_container_width=True, hide_index=True)

        st.markdown('<div class="category-header">🔹 Risk Management</div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame({
            "Parametre": ["risk_per_trade", "max_drawdown", "max_daily_trades"],
            "Range": ["0.5% - 2.0%", "5% - 10%", "3 - 15"],
            "Default": ["1%", "8%", 10],
            "Impact": ["🟡 MOYEN", "🟡 MOYEN", "🟢 BAS"]
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
    <p>Version 4.0 PRO - Ordre Revise Impact Maximum</p>
    <p>Decembre 2025</p>
</div>
""", unsafe_allow_html=True)
