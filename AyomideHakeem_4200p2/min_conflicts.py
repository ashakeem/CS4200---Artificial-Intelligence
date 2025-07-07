import random
from board import Board, N

def solve(board, max_steps=10000):
    """Min-conflicts algorithm. Mutates board in-place. Returns (solved, steps)."""
    for step in range(max_steps):
        if board.heuristic() == 0:
            return True, step

        conflicted_rows = [row for row in range(N) 
                          if board.conflicts_for_row(row, board.state[row]) > 0]
        
        if not conflicted_rows:
            return True, step

        row = random.choice(conflicted_rows)
        conflicts_per_col = [board.conflicts_for_row(row, col) for col in range(N)]
        min_conflict = min(conflicts_per_col)
        best_cols = [col for col, val in enumerate(conflicts_per_col) if val == min_conflict]
        
        board.state[row] = random.choice(best_cols)

    return False, max_steps 