import sys
from puzzle_input import generate_random_solvable_puzzle, read_puzzle_from_input, is_solvable
from heuristics import h1_misplaced_tiles, h2_manhattan_distance
from astar import astar, get_goal_state
from state import State

def print_grid(grid):
    for row in grid:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))

def print_solution(path):
    for idx, state in enumerate(path[1:], 1):
        print(f"Step: {idx}")
        print_grid(state.grid)

def single_test():
    print("Select Input Method:")
    print("[1] Random")
    print("[2] File")
    method = input().strip()
    if method == '1':
        while True:
            try:
                depth = int(input("Enter Solution Depth (2-20): ").strip())
                if 2 <= depth <= 20:
                    break
                else:
                    print("Depth must be between 2 and 20.")
            except ValueError:
                print("Invalid input. Enter an integer.")
        while True:
            grid = generate_random_solvable_puzzle()
            path, _, _ = astar(grid, h2_manhattan_distance)
            if len(path) - 1 >= depth:
                break
    else:
        grid = read_puzzle_from_input()
    print("Puzzle:")
    print_grid(grid)
    print("Select H Function:")
    print("[1] H1")
    print("[2] H2")
    h_choice = input().strip()
    heuristic = h1_misplaced_tiles if h_choice == '1' else h2_manhattan_distance
    path, nodes, runtime = astar(grid, heuristic)
    if not path:
        print("No solution found.")
        return
    print("Solution Found")
    print_solution([State(grid)] + path)  # include initial state as step 0
    print(f"Search Cost: {nodes}")
    print(f"Time: {runtime:.6f}")

def multi_test():
    print("Running multi-test harness...")
    from testing_harness import run_tests
    run_tests()

def main():
    print("CS 4200 Project 1")
    while True:
        print("Select:")
        print("[1] Single Test Puzzle")
        print("[2] Multi-Test Puzzle")
        print("[3] Exit")
        choice = input().strip()
        if choice == '1':
            single_test()
        elif choice == '2':
            multi_test()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main() 