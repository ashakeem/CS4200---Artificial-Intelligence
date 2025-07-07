import random
from board import Board

def solve(board, max_steps=1000):
    """Steepest-ascent hill climbing. Returns (solved, steps)."""
    current = board.copy()
    steps = 0

    while steps < max_steps:
        if current.heuristic() == 0:
            return True, steps

        neighbors = current.neighbors()
        heuristics = [nb.heuristic() for nb in neighbors]
        min_h = min(heuristics)

        if min_h >= current.heuristic():
            return False, steps  # Stuck in local optimum

        best_neighbors = [nb for nb, h in zip(neighbors, heuristics) if h == min_h]
        current = random.choice(best_neighbors)
        steps += 1

    return False, steps 