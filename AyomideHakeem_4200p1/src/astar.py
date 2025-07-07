import heapq
import time
from typing import Callable, List, Tuple, Optional, Set
from state import State

def get_goal_state() -> List[List[int]]:
    return [[1,2,3],[4,5,6],[7,8,0]]

def get_neighbors(state: State) -> List[State]:
    neighbors = []
    x, y = state.find_blank()
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_grid = [row[:] for row in state.grid]
            new_grid[x][y], new_grid[nx][ny] = new_grid[nx][ny], new_grid[x][y]
            neighbors.append(State(new_grid, state.g+1, 0, state))
    return neighbors

def astar(start_grid: List[List[int]], heuristic: Callable[[List[List[int]], List[List[int]]], int]) -> Tuple[List[State], int, float]:
    goal_grid = get_goal_state()
    start = State(start_grid, g=0, h=heuristic(start_grid, goal_grid))
    open_heap = [start]
    heapq.heapify(open_heap)
    closed_set: Set[int] = set()
    nodes_generated = 0
    start_time = time.time()
    while open_heap:
        current = heapq.heappop(open_heap)
        nodes_generated += 1
        if current.grid == goal_grid:
            end_time = time.time()
            path = []
            while current:
                path.append(current)
                current = current.parent
            path.reverse()
            return path, nodes_generated, end_time - start_time
        closed_set.add(hash(current))
        for neighbor in get_neighbors(current):
            if hash(neighbor) in closed_set:
                continue
            neighbor.h = heuristic(neighbor.grid, goal_grid)
            neighbor.f = neighbor.g + neighbor.h
            heapq.heappush(open_heap, neighbor)
    return [], nodes_generated, time.time() - start_time 