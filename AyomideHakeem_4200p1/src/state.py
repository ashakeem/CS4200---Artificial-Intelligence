import copy
from typing import Optional, List, Tuple

class State:
    def __init__(self, grid: List[List[int]], g: int = 0, h: int = 0, parent: Optional['State'] = None):
        self.grid = [row[:] for row in grid]
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __eq__(self, other):
        return isinstance(other, State) and self.grid == other.grid

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.grid))

    def __lt__(self, other):
        return self.f < other.f

    def find_blank(self) -> Tuple[int, int]:
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return i, j
        raise ValueError('No blank (0) in grid')

    def copy(self) -> 'State':
        return State(copy.deepcopy(self.grid), self.g, self.h, self.parent) 