# streamlit_app.py
import streamlit as st
import pandas as pd
from prisoners_dilemma_ai.strategies import (
    AlwaysConfess,
    AlwaysOpponentsLastMove,
    AlwaysStaySilent,
)
from prisoners_dilemma_ai.rl_agent import QLearningAgent
from prisoners_dilemma_ai.game import play_round

# ---------------------------
# Select Opponent (only once)
# ---------------------------
st.title("🎲 Prisoner's Dilemma: Q-Learning in Real Time")

opponent_options = {
    "Always Confess": AlwaysConfess,
    "Always Stay Silent": AlwaysStaySilent,
    "Tit for Tat": AlwaysOpponentsLastMove,
}

if "opponent_type" not in st.session_state:
    opponent_name = st.selectbox("Choose opponent type:", list(opponent_options.keys()))
    if st.button("Start Simulation"):
        # Save opponent type and initialize simulation
        st.session_state.opponent_type = opponent_name
        st.session_state.agent = QLearningAgent()
        st.session_state.opponent = opponent_options[opponent_name]()
        st.session_state.history = []
        st.session_state.round = 0
        st.session_state.score = 0
        st.rerun()
    st.stop()

# ------------------------------------
# Main simulation (after selection)
# ------------------------------------
st.success(f"Playing against: {st.session_state.opponent_type}")

if st.button("▶️ Play next round"):
    m1, m2, r1, r2 = play_round(st.session_state.agent, st.session_state.opponent)
    # st.session_state.score += r1
    st.session_state.history.append(
        {
            "Round": st.session_state.round + 1,
            "AI": m1,
            "Opponent": m2,
            "Reward": r1,
            # "Accumulated": st.session_state.score,
        }
    )
    st.session_state.round += 1

# Show round history
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.subheader("📜 Rounds History")
    st.dataframe(df, use_container_width=True, hide_index=True)
    # st.line_chart(df["Accumulated"])

    # Show Q-table
    qtable_raw = st.session_state.agent.q_table
    q_data = [
        {"State": str(k[0]), "Action": str(k[1]), "Q-value": v}
        for k, v in qtable_raw.items()
    ]
    q_df = pd.DataFrame(q_data).pivot(index="State", columns="Action", values="Q-value")
    st.subheader("🧠 Q-Table Learned")
    st.dataframe(q_df.style.background_gradient(cmap="RdYlGn"))

# Optional: Reset button
if st.button("🔁 Reset Simulation"):
    for key in ["opponent_type", "agent", "opponent", "history", "round", "score"]:
        st.session_state.pop(key, None)
    st.rerun()
