from typing import Literal

from prisoners_dilemma_ai.strategies import (
    AlwaysConfess,
    AlwaysStaySilent,
    AlwaysOpponentsLastMove,
    Move,
)

from prisoners_dilemma_ai.rl_agent import QLearningAgent


Player = AlwaysConfess | AlwaysStaySilent | AlwaysOpponentsLastMove | QLearningAgent


# C: Cooperate / stay silent; D: Defect / confess
# noinspection PyTypeChecker
PAYOFFS: dict[tuple[str, str], Literal[0, 1, 5, 10]] = {
    ("Silent", "Silent"): (1, 1),
    ("Confess", "Silent"): (0, 10),
    ("Silent", "Confess"): (10, 0),
    ("Confess", "Confess"): (5, 5),
}


def play_round(p1: Player, p2: Player) -> tuple[Move, Move, float, float]:
    print("\nNew round:")
    move1 = p1.play()
    move2 = p2.play()
    print(f"{p1.name}: {move1}")
    print(f"{p2.name}: {move2}")
    sentence1, sentence2 = PAYOFFS[(move1, move2)]
    p1.update(current_move=move1, opponents_current_move=move2, sentence=sentence1)
    p2.update(current_move=move2, opponents_current_move=move1, sentence=sentence2)
    return move1, move2, sentence1, sentence2
