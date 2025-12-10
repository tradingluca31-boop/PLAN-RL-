"""
DASHBOARD OPTUNA INTEGRE - Trading RL Gold
Version 5.0 - CONNEXION DIRECTE AUX ETUDES OPTUNA
"""

import streamlit as st
import pandas as pd
import os
from pathlib import Path

# Optuna import (optionnel si pas installé sur Streamlit Cloud)
try:
    import optuna
    OPTUNA_AVAILABLE = True
except ImportError:
    OPTUNA_AVAILABLE = False

st.set_page_config(
    page_title="Dashboard Optuna - RL Trading Gold",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemins vers les bases Optuna
OPTUNA_PATHS = {
    'rl_params': Path(r"C:\Users\lbye3\Desktop\AGENT 8 UNIQUEMENT\training\optuna_study.db"),
    'rewards': Path(r"C:\Users\lbye3\Desktop\AGENT 8 UNIQUEMENT\training\optuna_reward.db"),
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
    .main-header h1 { color: #ffd700; font-size: 2.5rem; margin-bottom: 10px; }
    .main-header p { color: #e8e8e8; font-size: 1.2rem; }
    .study-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f5);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 2px solid #e0e0e0;
    }
    .study-card-done { background: linear-gradient(145deg, #e8f5e9, #c8e6c9); border: 2px solid #4caf50; }
    .study-card-running { background: linear-gradient(145deg, #fff3e0, #ffe0b2); border: 2px solid #ff9800; }
    .study-card-pending { background: linear-gradient(145deg, #fce4ec, #f8bbd9); border: 2px solid #e91e63; }
    .metric-box {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white; padding: 20px; border-radius: 15px; text-align: center;
        margin: 5px;
    }
    .metric-value { font-size: 2rem; font-weight: 700; color: #ffd700; }
    .metric-label { font-size: 0.9rem; opacity: 0.9; }
    .best-params {
        background: linear-gradient(135deg, #4caf50, #8bc34a);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .param-row { display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid rgba(255,255,255,0.2); }
    .progress-container { background: #e0e0e0; border-radius: 25px; height: 30px; margin: 20px 0; overflow: hidden; }
    .progress-bar {
        background: linear-gradient(90deg, #4caf50, #8bc34a);
        height: 100%; border-radius: 25px;
        display: flex; align-items: center; justify-content: center;
        color: white; font-weight: 700;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# FONCTIONS OPTUNA
# =============================================================================

def load_optuna_study(db_path: Path, study_name: str = None):
    """Charge une étude Optuna depuis une base SQLite"""
    if not OPTUNA_AVAILABLE:
        return None
    if not db_path.exists():
        return None

    try:
        storage = f"sqlite:///{db_path}"
        studies = optuna.study.get_all_study_names(storage)

        if not studies:
            return None

        # Prendre la première étude ou celle spécifiée
        study_name = study_name or studies[0]
        study = optuna.load_study(study_name=study_name, storage=storage)
        return study
    except Exception as e:
        st.error(f"Erreur chargement étude: {e}")
        return None

def get_study_stats(study):
    """Extrait les statistiques d'une étude"""
    if study is None:
        return None

    trials = study.trials
    completed = [t for t in trials if t.state == optuna.trial.TrialState.COMPLETE]

    if not completed:
        return {
            'n_trials': 0,
            'n_completed': 0,
            'best_value': None,
            'best_params': {},
            'status': 'pending'
        }

    return {
        'n_trials': len(trials),
        'n_completed': len(completed),
        'best_value': study.best_value,
        'best_params': study.best_params,
        'status': 'done' if len(completed) >= 50 else 'running'
    }

# =============================================================================
# HEADER
# =============================================================================

st.markdown("""
<div class="main-header">
    <h1>🔬 DASHBOARD OPTUNA INTEGRE</h1>
    <p>Connexion Directe aux Études Optuna - Agent 8 RL Trading Gold</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# SIDEBAR - CONFIGURATION
# =============================================================================

with st.sidebar:
    st.markdown("## ⚙️ Configuration")

    st.markdown("### 📂 Chemins Optuna")

    # Permettre de modifier les chemins
    rl_params_path = st.text_input(
        "Étude Hyperparamètres RL",
        value=str(OPTUNA_PATHS['rl_params']),
        key="path_rl"
    )

    rewards_path = st.text_input(
        "Étude Rewards",
        value=str(OPTUNA_PATHS['rewards']),
        key="path_rewards"
    )

    # Upload de fichier .db (pour Streamlit Cloud)
    st.markdown("---")
    st.markdown("### 📤 Ou Uploader des fichiers .db")

    uploaded_rl = st.file_uploader("Upload optuna_study.db", type=['db'], key="upload_rl")
    uploaded_reward = st.file_uploader("Upload optuna_reward.db", type=['db'], key="upload_reward")

    if uploaded_rl:
        # Sauvegarder temporairement
        temp_path = Path("/tmp/optuna_study.db")
        with open(temp_path, 'wb') as f:
            f.write(uploaded_rl.read())
        rl_params_path = str(temp_path)

    if uploaded_reward:
        temp_path = Path("/tmp/optuna_reward.db")
        with open(temp_path, 'wb') as f:
            f.write(uploaded_reward.read())
        rewards_path = str(temp_path)

# =============================================================================
# CHARGEMENT DES ETUDES
# =============================================================================

studies_data = {}

# Étude 1: Hyperparamètres RL
study_rl = load_optuna_study(Path(rl_params_path))
studies_data['rl_params'] = get_study_stats(study_rl)

# Étude 2: Rewards
study_reward = load_optuna_study(Path(rewards_path))
studies_data['rewards'] = get_study_stats(study_reward)

# =============================================================================
# METRIQUES GLOBALES
# =============================================================================

total_studies = 2
completed_studies = sum(1 for s in studies_data.values() if s and s.get('status') == 'done')
running_studies = sum(1 for s in studies_data.values() if s and s.get('status') == 'running')
total_trials = sum(s.get('n_completed', 0) for s in studies_data.values() if s)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="metric-box"><div class="metric-value">{total_trials}</div><div class="metric-label">Trials Complétés</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-box"><div class="metric-value">{completed_studies}/8</div><div class="metric-label">Études Terminées</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-box"><div class="metric-value">{running_studies}</div><div class="metric-label">En Cours</div></div>', unsafe_allow_html=True)
with col4:
    best_roi = None
    if studies_data['rl_params'] and studies_data['rl_params'].get('best_value'):
        best_roi = studies_data['rl_params']['best_value']
    st.markdown(f'<div class="metric-box"><div class="metric-value">{best_roi:.2f}%</div><div class="metric-label">Meilleur ROI</div></div>' if best_roi else '<div class="metric-box"><div class="metric-value">-</div><div class="metric-label">Meilleur ROI</div></div>', unsafe_allow_html=True)

progress_pct = int((completed_studies / 8) * 100)
st.markdown(f'<div class="progress-container"><div class="progress-bar" style="width: {max(progress_pct, 5)}%;">{progress_pct}% Optimisation Complète</div></div>', unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# ETUDE 1: HYPERPARAMETRES RL
# =============================================================================

st.markdown("## 📊 Études Optuna Détectées")

col1, col2 = st.columns(2)

with col1:
    stats = studies_data['rl_params']
    if stats:
        status_class = f"study-card-{stats['status']}"
        status_emoji = "✅" if stats['status'] == 'done' else "🔄" if stats['status'] == 'running' else "⏳"

        st.markdown(f"""
        <div class="study-card {status_class}">
            <h3>{status_emoji} Étude 1: Hyperparamètres RL</h3>
            <p><strong>Fichier:</strong> optuna_study.db</p>
            <p><strong>Trials:</strong> {stats['n_completed']} complétés</p>
            <p><strong>Meilleur Score:</strong> {stats['best_value']:.4f if stats['best_value'] else 'N/A'}</p>
        </div>
        """, unsafe_allow_html=True)

        if stats['best_params']:
            with st.expander("🏆 MEILLEURS PARAMETRES TROUVES", expanded=True):
                params_df = pd.DataFrame([
                    {"Paramètre": k, "Valeur Optimale": f"{v:.6f}" if isinstance(v, float) else str(v)}
                    for k, v in stats['best_params'].items()
                ])
                st.dataframe(params_df, use_container_width=True, hide_index=True)
    else:
        st.markdown("""
        <div class="study-card study-card-pending">
            <h3>⏳ Étude 1: Hyperparamètres RL</h3>
            <p><strong>Status:</strong> Non trouvée ou vide</p>
            <p>Upload le fichier optuna_study.db dans la sidebar</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    stats = studies_data['rewards']
    if stats:
        status_class = f"study-card-{stats['status']}"
        status_emoji = "✅" if stats['status'] == 'done' else "🔄" if stats['status'] == 'running' else "⏳"

        st.markdown(f"""
        <div class="study-card {status_class}">
            <h3>{status_emoji} Étude 2: Fonction de Reward</h3>
            <p><strong>Fichier:</strong> optuna_reward.db</p>
            <p><strong>Trials:</strong> {stats['n_completed']} complétés</p>
            <p><strong>Meilleur Score:</strong> {stats['best_value']:.4f if stats['best_value'] else 'N/A'}</p>
        </div>
        """, unsafe_allow_html=True)

        if stats['best_params']:
            with st.expander("🏆 MEILLEURS PARAMETRES TROUVES", expanded=True):
                params_df = pd.DataFrame([
                    {"Paramètre": k, "Valeur Optimale": f"{v:.6f}" if isinstance(v, float) else str(v)}
                    for k, v in stats['best_params'].items()
                ])
                st.dataframe(params_df, use_container_width=True, hide_index=True)
    else:
        st.markdown("""
        <div class="study-card study-card-pending">
            <h3>⏳ Étude 2: Fonction de Reward</h3>
            <p><strong>Status:</strong> Non trouvée ou vide</p>
            <p>Upload le fichier optuna_reward.db dans la sidebar</p>
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# ETUDES A CREER
# =============================================================================

st.markdown("---")
st.markdown("## 📋 Études Restantes à Créer")

remaining_studies = [
    {
        'name': 'Features Selection',
        'description': 'Sélection des meilleures features (SHAP, importance)',
        'db_name': 'optuna_features.db',
        'params': ['n_features', 'use_momentum', 'use_cot', 'scaler_type']
    },
    {
        'name': 'Architecture Réseau',
        'description': 'Taille et forme du réseau de neurones',
        'db_name': 'optuna_architecture.db',
        'params': ['n_layers', 'layer_size', 'net_arch_pattern']
    },
    {
        'name': 'Indicateurs Techniques',
        'description': 'Périodes RSI, MACD, BB, ATR',
        'db_name': 'optuna_indicators.db',
        'params': ['rsi_period', 'macd_fast', 'macd_slow', 'bb_period']
    },
    {
        'name': 'Filtres Volatilité',
        'description': 'Quand trader (ATR, BB width)',
        'db_name': 'optuna_volatility.db',
        'params': ['atr_filter_min', 'atr_filter_max', 'bb_width_min']
    },
    {
        'name': 'Filtres Temporels',
        'description': 'Sessions, jours, news buffer',
        'db_name': 'optuna_temporal.db',
        'params': ['trade_london', 'trade_ny', 'news_buffer']
    },
    {
        'name': 'SL/TP & Risk',
        'description': 'Stop Loss, Take Profit, Risk par trade',
        'db_name': 'optuna_sltp.db',
        'params': ['sl_atr_mult', 'tp_rr_ratio', 'risk_per_trade']
    }
]

cols = st.columns(3)
for i, study in enumerate(remaining_studies):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="study-card study-card-pending">
            <h4>⏳ {study['name']}</h4>
            <p style="font-size: 0.9rem; color: #666;">{study['description']}</p>
            <p style="font-size: 0.8rem;"><strong>DB:</strong> {study['db_name']}</p>
            <p style="font-size: 0.8rem;"><strong>Params:</strong> {', '.join(study['params'][:3])}...</p>
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# GUIDE RAPIDE
# =============================================================================

st.markdown("---")
st.markdown("## 🚀 Guide Rapide - Créer une Nouvelle Étude")

with st.expander("📝 Template Optuna pour nouvelle étude", expanded=False):
    st.code("""
import optuna
from optuna.samplers import TPESampler
from optuna.pruners import MedianPruner

def objective(trial):
    # Suggérer les paramètres
    param1 = trial.suggest_float('learning_rate', 1e-5, 1e-3, log=True)
    param2 = trial.suggest_int('n_steps', 512, 4096, step=512)
    param3 = trial.suggest_categorical('net_arch', ['small', 'medium', 'large'])

    # Créer et entraîner l'environnement
    # ...

    # Retourner la métrique à optimiser
    return roi_pct  # ou -roi_pct si minimize

# Créer l'étude
study = optuna.create_study(
    study_name="nouvelle_etude",
    storage="sqlite:///optuna_nouvelle.db",
    direction="maximize",  # ou "minimize"
    sampler=TPESampler(seed=42),
    pruner=MedianPruner(n_startup_trials=10)
)

# Lancer l'optimisation
study.optimize(objective, n_trials=100, timeout=3600*6)

# Afficher les meilleurs paramètres
print(f"Best value: {study.best_value}")
print(f"Best params: {study.best_params}")
""", language="python")

# =============================================================================
# VISUALISATIONS OPTUNA
# =============================================================================

if OPTUNA_AVAILABLE and (study_rl or study_reward):
    st.markdown("---")
    st.markdown("## 📈 Visualisations Optuna")

    viz_study = study_rl if study_rl else study_reward
    study_name = "Hyperparamètres RL" if study_rl else "Rewards"

    if viz_study and len(viz_study.trials) > 0:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"### Historique d'Optimisation - {study_name}")
            try:
                fig = optuna.visualization.plot_optimization_history(viz_study)
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.warning(f"Impossible de créer le graphique: {e}")

        with col2:
            st.markdown(f"### Importance des Paramètres - {study_name}")
            try:
                fig = optuna.visualization.plot_param_importances(viz_study)
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.warning(f"Impossible de créer le graphique: {e}")

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666;">
    <p><strong>Dashboard Optuna Intégré - Agent 8 RL Trading Gold</strong></p>
    <p>Version 5.0 - Connexion Directe aux Études</p>
    <p>Décembre 2025</p>
</div>
""", unsafe_allow_html=True)
