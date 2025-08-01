from typing import Literal
import random


Move = Literal["Confess", "Silent"]


class AlwaysConfess:
    def __init__(self):
        self.name = "Always Confess"

    def play(self) -> Move:
        return "Confess"  # Cooperate with police: confess

    def update(
        self,
        my_current_move: Move,
        opponents_current_move: Move,
        sentence: Literal[0, 1, 5, 10],
    ):
        pass


class AlwaysStaySilent:
    def __init__(self):
        self.name = "Always Stay Silent"

    def play(self) -> Move:
        return "Silent"  # Defect: do not cooperate with police

    def update(
        self,
        my_current_move: Move,
        opponents_current_move: Move,
        sentence: Literal[0, 1, 5, 10],
    ):
        pass


class AlwaysOpponentsLastMove:
    def __init__(self):
        self.name = "Last Opponent Move"
        self.last_opponent_move: Move = random.choice(["Confess", "Silent"])

    def play(self) -> Move:
        return self.last_opponent_move

    def update(
        self,
        my_current_move: Move,
        opponents_current_move: Move,
        sentence: Literal[0, 1, 5, 10],
    ) -> None:
        self.last_opponent_move = opponents_current_move
