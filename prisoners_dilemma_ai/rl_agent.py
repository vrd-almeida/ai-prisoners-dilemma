import random
from typing import Literal


Move = Literal["Confess", "Silent"]


class QLearningAgent:
    def __init__(self, alpha=0.2, gamma=0.1, epsilon=0.95):
        self.name = "Q-Learner"
        self.q_table = {}  # (last_opponent_move, action): value
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.last_opponent_move: None | Move = None
        self.last_action: None | Move = None

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
        old_q = self.q_table.get((self.last_opponent_move, self.last_action), 0.0)
        future_q = max(
            self.q_table.get((opponents_current_move, a), 0.0)
            for a in ["Confess", "Silent"]
        )
        sentence_to_reward_map = {10: 0, 5: 5, 1: 9, 0: 10}
        reward = sentence_to_reward_map[sentence]
        new_q = old_q + self.alpha * (1 - self.epsilon) * (
            reward + self.gamma * (future_q - old_q)
        )
        self.last_action = current_move
        self.last_opponent_move = opponents_current_move
        self.q_table[(self.last_opponent_move, self.last_action)] = new_q
        print(self.q_table)


#
# import random
# from typing import Literal
#
#
# Move = Literal["Confess", "Silent"]
#
#
# class QLearningAgent:
#     def __init__(self, alpha=0.1, gamma=0.95, epsilon=0.1):
#         self.name = "Q-Learner"
#         self.q_table = {}  # (state, action): value
#         self.alpha = alpha  # learning rate
#         self.gamma = gamma  # discount factor
#         self.epsilon = epsilon  # exploration rate
#         self.last_opponent_move: None | Move = None
#         self.last_action: None | Move = None
#
#     def get_q_value(self, state: Move | None, action: Move):
#         return self.q_table.get((state, action), 0.0)
#
#     def choose_action(self, state: Move | None) -> Move:
#         random_value = random.random()
#         if random_value < self.epsilon:
#             return random.choice(["Confess", "Silent"])  # explore
#         else:
#             q_c = self.get_q_value(state, "Confess")
#             q_d = self.get_q_value(state, "Silent")
#             return "Confess" if q_c > q_d else "Silent"  # exploit
#
#     def play(self, opponent_last_move: None | Move = None) -> Move:
#         # Use opponent's last move as state
#         state = opponent_last_move
#         action = self.choose_action(state)
#         print(f"state: {state}, action: {action}")
#         self.last_opponent_move = state
#         self.last_action = action
#         return action
#
#     def update(
#         self, my_move, opponent_move: Move, reward: Literal[0, 1, 5, 10]
#     ) -> None:
#         new_state = opponent_move
#         old_q = self.get_q_value(self.last_opponent_move, self.last_action)
#         future_q = max(self.get_q_value(new_state, a) for a in ["Confess", "Silent"])
#         new_q = old_q + self.alpha * (reward + self.gamma * future_q - old_q)
#         self.q_table[(self.last_opponent_move, self.last_action)] = new_q
