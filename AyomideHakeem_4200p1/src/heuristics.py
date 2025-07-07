from typing import List

def h1_misplaced_tiles(state: List[List[int]], goal: List[List[int]]) -> int:
    return sum(
        1 for i in range(3) for j in range(3)
        if state[i][j] != 0 and state[i][j] != goal[i][j]
    )

def h2_manhattan_distance(state: List[List[int]], goal: List[List[int]]) -> int:
    pos = {}
    for i in range(3):
        for j in range(3):
            pos[goal[i][j]] = (i, j)
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gi, gj = pos[val]
                dist += abs(i - gi) + abs(j - gj)
    return dist 