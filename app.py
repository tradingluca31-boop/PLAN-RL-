"""
DASHBOARD OPTUNA - Trading RL Gold Agent 8
Version 6.0 - CE QUI PEUT REELLEMENT ETRE OPTIMISE
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Optuna Agent 8 - RL Trading Gold",
    page_icon="🔬",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .main-header h1 { color: #ffd700; font-size: 2.2rem; margin-bottom: 5px; }
    .main-header p { color: #e8e8e8; font-size: 1.1rem; }
    .done-card {
        background: linear-gradient(145deg, #e8f5e9, #c8e6c9);
        border: 2px solid #4caf50;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    .todo-card {
        background: linear-gradient(145deg, #fff3e0, #ffe0b2);
        border: 2px solid #ff9800;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    .param-table { background: #f5f5f5; border-radius: 10px; padding: 15px; margin: 10px 0; }
    .metric-box {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white; padding: 15px; border-radius: 10px; text-align: center;
    }
    .metric-value { font-size: 1.8rem; font-weight: 700; color: #ffd700; }
    .metric-label { font-size: 0.85rem; opacity: 0.9; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="main-header">
    <h1>🔬 OPTUNA AGENT 8 - RL Trading Gold</h1>
    <p>Ce qui peut REELLEMENT etre optimise avec Optuna</p>
</div>
""", unsafe_allow_html=True)

# METRICS
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-box"><div class="metric-value">2/5</div><div class="metric-label">Phases Terminees</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-box"><div class="metric-value">150</div><div class="metric-label">Trials Total</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-box"><div class="metric-value">+7.79%</div><div class="metric-label">Best ROI</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-box"><div class="metric-value">~21h</div><div class="metric-label">Temps Passe</div></div>', unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# PHASE 1: RL PARAMS - DONE
# =============================================================================
st.markdown("## ✅ Phase 1: Hyperparametres PPO (TERMINE)")

st.markdown("""
<div class="done-card">
    <h3>✅ BEST_HP - 100 trials, 15h, +2.63% ROI</h3>
    <p>Fichier: <code>config_agent8.py</code> ligne 44-64</p>
</div>
""", unsafe_allow_html=True)

with st.expander("Voir les parametres optimises", expanded=False):
    st.dataframe(pd.DataFrame({
        "Parametre": ["learning_rate", "gamma", "gae_lambda", "clip_range", "vf_coef", "max_grad_norm",
                      "ent_coef_start", "ent_coef_end", "n_steps", "batch_size", "n_epochs", "net_arch"],
        "Valeur Optuna": ["1.57e-05", "0.9662", "0.9101", "0.12", "0.6742", "0.7985",
                         "0.3711", "0.0901", "1024", "64", "12", "[128, 128]"],
        "Status": ["✅"] * 12
    }), use_container_width=True, hide_index=True)

# =============================================================================
# PHASE 2: REWARDS - DONE
# =============================================================================
st.markdown("## ✅ Phase 2: Fonction de Reward (TERMINE)")

st.markdown("""
<div class="done-card">
    <h3>✅ BEST_REWARD - 50 trials, 6.5h, +7.79% ROI</h3>
    <p>Fichier: <code>config_agent8.py</code> ligne 73-108</p>
</div>
""", unsafe_allow_html=True)

with st.expander("Voir les parametres optimises", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Trade Actions**")
        st.dataframe(pd.DataFrame({
            "Parametre": ["open_reward", "win_close_reward", "loss_close_penalty"],
            "Valeur": ["1.7614", "5.3991", "-14.3543"]
        }), use_container_width=True, hide_index=True)

        st.markdown("**Demonstration Phases**")
        st.dataframe(pd.DataFrame({
            "Parametre": ["demo_phase1_bonus", "demo_phase2_bonus", "demo_phase3_bonus"],
            "Valeur": ["10.8445", "7.6290", "7.3026"]
        }), use_container_width=True, hide_index=True)

    with col2:
        st.markdown("**Anti-Mode Collapse**")
        st.dataframe(pd.DataFrame({
            "Parametre": ["passivity_penalty", "repetition_penalty", "diversity_threshold"],
            "Valeur": ["-8.3714", "-0.9029", "0.7288"]
        }), use_container_width=True, hide_index=True)

        st.markdown("**Tier Weights**")
        st.dataframe(pd.DataFrame({
            "Parametre": ["core_weight", "risk_weight", "diversity_weight"],
            "Valeur": ["0.4934", "0.2008", "0.2896"]
        }), use_container_width=True, hide_index=True)

st.markdown("---")

# =============================================================================
# PHASE 3: SL/TP - TODO
# =============================================================================
st.markdown("## ⏳ Phase 3: SL/TP & Risk (A FAIRE)")

st.markdown("""
<div class="todo-card">
    <h3>⏳ Stop Loss / Take Profit - NON OPTIMISE</h3>
    <p>Fichier: <code>trading_env.py</code> ligne 502-506</p>
    <p><strong>Impact:</strong> 🔴 CRITIQUE - Determine Win Rate et ROI</p>
</div>
""", unsafe_allow_html=True)

with st.expander("Parametres a optimiser", expanded=True):
    st.dataframe(pd.DataFrame({
        "Parametre": ["RISK_REWARD_RATIO", "ATR_MULTIPLIER (stop)", "SLIPPAGE_PIPS"],
        "Valeur Actuelle": ["4.0", "2.5", "0.3"],
        "Range Optuna": ["[2.0, 3.0, 4.0, 5.0]", "[1.5, 2.0, 2.5, 3.0, 3.5]", "[0.1, 0.2, 0.3, 0.5]"],
        "Impact": ["🔴 CRITIQUE", "🔴 CRITIQUE", "🟡 MOYEN"]
    }), use_container_width=True, hide_index=True)

    st.code("""
# Dans trading_env.py ligne 502:
self.RISK_REWARD_RATIO = trial.suggest_categorical("rr_ratio", [2.0, 3.0, 4.0, 5.0])

# Dans trading_env.py ligne 833:
atr_mult = trial.suggest_float("atr_mult", 1.5, 3.5)
stop_distance = atr * atr_mult
""", language="python")

# =============================================================================
# PHASE 4: RSI THRESHOLDS - TODO
# =============================================================================
st.markdown("## ⏳ Phase 4: RSI Thresholds (A FAIRE)")

st.markdown("""
<div class="todo-card">
    <h3>⏳ Seuils RSI Mean Reversion - NON OPTIMISE</h3>
    <p>Fichier: <code>trading_env.py</code> ligne 804-805</p>
    <p><strong>Impact:</strong> 🟡 MOYEN - Timing des entrees</p>
</div>
""", unsafe_allow_html=True)

with st.expander("Parametres a optimiser", expanded=True):
    st.dataframe(pd.DataFrame({
        "Parametre": ["RSI_OVERSOLD", "RSI_OVERBOUGHT", "RSI_PERIOD"],
        "Valeur Actuelle": ["40", "60", "14"],
        "Range Optuna": ["[25, 30, 35, 40]", "[60, 65, 70, 75]", "[7, 14, 21]"],
        "Impact": ["🟡 MOYEN", "🟡 MOYEN", "🟢 BAS"]
    }), use_container_width=True, hide_index=True)

    st.code("""
# Dans trading_env.py ligne 804-805:
rsi_oversold = trial.suggest_int("rsi_oversold", 25, 40, step=5)
rsi_overbought = trial.suggest_int("rsi_overbought", 60, 75, step=5)
""", language="python")

# =============================================================================
# PHASE 5: FEATURES - TODO
# =============================================================================
st.markdown("## ⏳ Phase 5: Selection Features (A FAIRE)")

st.markdown("""
<div class="todo-card">
    <h3>⏳ Nombre et type de features - NON OPTIMISE</h3>
    <p>Fichier: <code>trading_env.py</code> - 222 features actuellement</p>
    <p><strong>Impact:</strong> 🟢 BAS - Fine-tuning</p>
</div>
""", unsafe_allow_html=True)

with st.expander("Parametres a optimiser", expanded=True):
    st.dataframe(pd.DataFrame({
        "Parametre": ["n_top_features", "use_cot_features", "use_macro_features", "use_volume_features"],
        "Valeur Actuelle": ["222 (toutes)", "True", "True", "True"],
        "Range Optuna": ["[50, 100, 150, 200]", "[True, False]", "[True, False]", "[True, False]"],
        "Impact": ["🟢 BAS", "🟢 BAS", "🟢 BAS", "🟢 BAS"]
    }), use_container_width=True, hide_index=True)

# =============================================================================
# SUMMARY
# =============================================================================
st.markdown("---")
st.markdown("## 📊 Resume")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Termine (2/5)")
    st.success("**Phase 1:** Hyperparametres PPO - 100 trials")
    st.success("**Phase 2:** Fonction Reward - 50 trials")

with col2:
    st.markdown("### ⏳ A Faire (3/5)")
    st.warning("**Phase 3:** SL/TP & Risk - 🔴 PRIORITE")
    st.info("**Phase 4:** RSI Thresholds")
    st.info("**Phase 5:** Selection Features")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p><strong>Agent 8 - Mean Reversion M15 - Gold Trading</strong></p>
    <p>Optuna Optimization Dashboard v6.0</p>
</div>
""", unsafe_allow_html=True)
