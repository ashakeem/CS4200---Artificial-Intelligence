import random
from typing import List, Tuple

def flatten(grid: List[List[int]]) -> List[int]:
    return [num for row in grid for num in row]

def count_inversions(arr: List[int]) -> int:
    arr = [x for x in arr if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def is_solvable(grid: List[List[int]]) -> bool:
    inv = count_inversions(flatten(grid))
    return inv % 2 == 0

def generate_random_solvable_puzzle() -> List[List[int]]:
    while True:
        nums = list(range(9))
        random.shuffle(nums)
        grid = [nums[i*3:(i+1)*3] for i in range(3)]
        if is_solvable(grid):
            return grid

def read_puzzle_from_input() -> List[List[int]]:
    print('Enter the puzzle configuration (use 0 for blank):')
    grid = []
    for i in range(3):
        while True:
            row = input(f'Row {i+1} (space-separated): ').strip().split()
            if len(row) == 3 and all(x.isdigit() and 0 <= int(x) <= 8 for x in row):
                grid.append([int(x) for x in row])
                break
            else:
                print('Invalid row. Please enter 3 numbers between 0 and 8.')
    if not is_solvable(grid):
        print('This puzzle is not solvable. Please try again.')
        return read_puzzle_from_input()
    return grid 