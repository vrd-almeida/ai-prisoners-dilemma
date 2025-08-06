# 🤖 Prisoner's Dilemma AI Simulation

A simulation framework for studying the classic **Prisoner’s Dilemma** using rule-based agents and reinforcement learning. This project allows agents to play iterated games, adapt strategies using **Q-learning**, and analyze emerging behavior such as cooperation, betrayal, or equilibrium.

---

# Streamlit Deployment

https://ai-prisoners-dilemma-tzx2rjmtv48mkthtwz4qym.streamlit.app/

---

## 📌 What is the Prisoner’s Dilemma?

The **Prisoner's Dilemma** is a famous problem in game theory that illustrates why individuals might not cooperate, even when it is in their best interest to do so.

Each of the two players can either:
- **Confess** (betray the other), or
- **Remain Silent** (cooperate).

The outcomes depend on the combination of choices:

| Player A       | Player B       | Years in Prison A | Years in Prison B |
|----------------|----------------|-------------------|-------------------|
| Silent         | Silent         | 1                 | 1                 |
| Confess        | Silent         | 0                 | 10                |
| Silent         | Confess        | 10                | 0                 |
| Confess        | Confess        | 5                 | 5                 |

In this project, we **invert the reward scale** so that **fewer years = higher reward**. This makes it compatible with reinforcement learning agents that aim to **maximize** reward.

---

## 🧠 Goals of This Project

- ✅ Simulate the Prisoner's Dilemma as an iterated game
- ✅ Implement basic agents with static strategies (Tit for Tat, Always Confess, etc.)
- ✅ Implement a **Q-learning agent** that learns the best strategy through trial and error
- ✅ Analyze the evolution of behavior over time
- ✅ Visualize score progression, cooperation rates, and learned Q-values

---

## 🧩 How It Works

### 🔁 Repeated Game
Each match consists of multiple rounds. After each round:
- Agents decide based on the opponent’s last move (if they can)
- Scores are assigned based on a payoff matrix
- The Q-learning agent updates its policy using the Q-learning algorithm

### 🧠 Q-learning Logic

Q-values are updated using the formula:

Q(s, a) ← Q(s, a) + α × [r + γ × max(Q(s', a')) − Q(s, a)]

yaml
Copier
Modifier

Where:
- `s` is the current state (opponent’s last move)
- `a` is the chosen action
- `r` is the reward received
- `s'` is the new state (next opponent move)
- `α` is the learning rate
- `γ` is the discount factor

---

## 🎮 Strategies Implemented

| Strategy        | Description                                             |
|-----------------|---------------------------------------------------------|
| AlwaysCooperate | Always plays "Silent"                                   |
| AlwaysDefect    | Always plays "Confess"                                  |
| TitForTat       | Starts with "Silent", then mimics opponent’s last move  |
| QLearningAgent  | Learns the best action using Q-learning from feedback   |

---

👨‍💻 Author
Vinicius Rodrigues De Almeida, PhD.

📍 Based in Lyon, France 🇫🇷

💡 Interests: optimization, machine learning, AI

🔗 https://www.linkedin.com/in/vinicius-rodrigues-de-almeida-2a575084/

