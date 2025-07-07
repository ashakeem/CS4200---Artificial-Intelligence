import random

N = 8

class Board:
    def __init__(self, state):
        self.state = list(state)

    @staticmethod
    def random():
        return Board([random.randint(0, N - 1) for _ in range(N)])

    def heuristic(self):
        """Number of attacking queen pairs; 0 = solution."""
        attacks = 0
        for i in range(N):
            for j in range(i + 1, N):
                if self.state[i] == self.state[j] or abs(self.state[i] - self.state[j]) == j - i:
                    attacks += 1
        return attacks

    def conflicts_for_row(self, row, col):
        """Conflicts if queen in `row` placed at `col`."""
        return sum(1 for r in range(N) if r != row and 
                  (self.state[r] == col or abs(self.state[r] - col) == abs(r - row)))

    def neighbors(self):
        """All boards by moving one queen within its row."""
        neighbors = []
        for row in range(N):
            for col in range(N):
                if col != self.state[row]:
                    new_state = list(self.state)
                    new_state[row] = col
                    neighbors.append(Board(new_state))
        return neighbors

    def copy(self):
        return Board(self.state)

    def __str__(self):
        return ",".join(str(c) for c in self.state)

    def display(self):
        """ASCII board with Q for queens, · for empty."""
        return "\n".join("".join("Q " if self.state[row] == col else "· " 
                               for col in range(N)).rstrip() for row in range(N)) 