from typing import Literal

from strategies import AlwaysConfess, AlwaysStaySilent, AlwaysOpponentsLastMove


Player = AlwaysConfess | AlwaysStaySilent | AlwaysOpponentsLastMove


# C: Cooperate / stay silent; D: Defect / confess
# noinspection PyTypeChecker
PAYOFFS: dict[tuple[str, str], Literal[0, 1, 5, 10]] = {
    ("Silent", "Silent"): (1, 1),
    ("Confess", "Silent"): (0, 10),
    ("Silent", "Confess"): (10, 0),
    ("Confess", "Confess"): (5, 5),
}


def play_round(p1: Player, p2: Player) -> tuple[float, float]:
    move1 = p1.play()
    move2 = p2.play()
    sentence1, sentence2 = PAYOFFS[(move1, move2)]
    p1.update(my_current_move=move1, opponents_current_move=move2, sentence=sentence1)
    p2.update(my_current_move=move2, opponents_current_move=move1, sentence=sentence2)
    return sentence1, sentence2
