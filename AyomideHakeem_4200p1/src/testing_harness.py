import csv
import random
from heuristics import h1_misplaced_tiles, h2_manhattan_distance
from astar import astar, get_goal_state
from puzzle_input import generate_random_solvable_puzzle

def get_depth(path):
    return len(path) - 1 if path else -1

def run_tests():
    results = []
    sample_runs = {"lt6": [], "6to12": [], "gt12": []}
    for i in range(120):
        # Generate a random puzzle with a specific depth
        while True:
            grid = generate_random_solvable_puzzle()
            path, _, _ = astar(grid, h2_manhattan_distance)
            depth = get_depth(path)
            if 2 <= depth <= 20:
                break
        for hname, heuristic in [("h1", h1_misplaced_tiles), ("h2", h2_manhattan_distance)]:
            path, nodes, runtime = astar(grid, heuristic)
            depth = get_depth(path)
            results.append({
                "puzzle": grid,
                "heuristic": hname,
                "depth": depth,
                "nodes": nodes,
                "runtime": runtime
            })
            # Save sample runs
            if hname == "h2":
                if depth < 6 and len(sample_runs["lt6"]) < 1:
                    sample_runs["lt6"].append((grid, path, nodes, runtime))
                elif 6 <= depth <= 12 and len(sample_runs["6to12"]) < 1:
                    sample_runs["6to12"].append((grid, path, nodes, runtime))
                elif depth > 12 and len(sample_runs["gt12"]) < 1:
                    sample_runs["gt12"].append((grid, path, nodes, runtime))
    # Write CSV
    with open("../results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["heuristic", "depth", "nodes", "runtime", "puzzle"])
        writer.writeheader()
        for row in results:
            writer.writerow({
                "heuristic": row["heuristic"],
                "depth": row["depth"],
                "nodes": row["nodes"],
                "runtime": f"{row['runtime']:.6f}",
                "puzzle": ' '.join(str(x) for r in row["puzzle"] for x in r)
            })
    # Write sample outputs
    for key, fname in zip(["lt6", "6to12", "gt12"], ["sample_lt6.txt", "sample_6to12.txt", "sample_gt12.txt"]):
        if sample_runs[key]:
            grid, path, nodes, runtime = sample_runs[key][0]
            with open(f"../{fname}", "w") as f:
                f.write("Initial State:\n")
                for row in grid:
                    f.write(' '.join(str(x) if x != 0 else ' ' for x in row) + '\n')
                f.write("\nSolution Steps:\n")
                for idx, state in enumerate(path):
                    f.write(f"Step {idx}:\n")
                    for row in state.grid:
                        f.write(' '.join(str(x) if x != 0 else ' ' for x in row) + '\n')
                    f.write("\n")
                f.write(f"Search Cost: {nodes}\n")
                f.write(f"Time Taken: {runtime:.6f} seconds\n")
    print("Testing complete. Results saved to results.csv and sample output files.") 