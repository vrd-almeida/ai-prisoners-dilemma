import random
from typing import Literal


Move = Literal["Confess", "Silent"]


class QLearningAgent:
    def __init__(self, alpha=0.5, gamma=0.5, epsilon=0.95):
        self.name = "Q-Learner"
        self.q_table = {}  # (last_opponent_move, action): value
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.last_opponent_move: None | Move = None  # type: ignore
        self.last_action: None | Move = None  # type: ignore

    def play(self) -> Move:
        action: Move
        random_value = random.random()
        if random_value < self.epsilon:
            action = random.choice(["Confess", "Silent"])  # explore
            self.epsilon = max(0.1, self.epsilon - 0.05)
        else:
            q_confess = self.q_table.get((self.last_opponent_move, "Confess"), 0.0)
            q_silent = self.q_table.get((self.last_opponent_move, "Silent"), 0.0)
            if q_confess > q_silent:
                action = "Confess"
            else:
                action = "Silent"
        return action

    def update(
        self,
        current_move: Move,
        opponents_current_move: Move,
        sentence: Literal[0, 1, 5, 10],
    ) -> None:
        old_q = self.q_table.get((opponents_current_move, current_move), 0.0)
        future_q = max(
            self.q_table.get((opponents_current_move, "Confess"), 0.0),
            self.q_table.get((opponents_current_move, "Silent"), 0.0),
        )
        sentence_to_reward_map = {10: 0, 5: 5, 1: 9, 0: 10}
        reward = sentence_to_reward_map[sentence]
        new_q = old_q + self.alpha * (reward + self.gamma * (future_q - old_q))
        self.last_action = current_move
        self.last_opponent_move = opponents_current_move
        self.q_table[(self.last_opponent_move, self.last_action)] = new_q
        print(self.q_table)
