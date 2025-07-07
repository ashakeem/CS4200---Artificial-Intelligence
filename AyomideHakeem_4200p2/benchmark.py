import argparse, csv, os, time
from board import Board
import hill_climbing, min_conflicts

def main():
    parser = argparse.ArgumentParser(description="Benchmark 8-queen solvers.")
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--show-progress", action="store_true")
    args = parser.parse_args()

    os.makedirs("samples", exist_ok=True)
    saved_samples = displayed_samples = 0

    print(f"Running {args.trials} trials...")
    if args.show_progress: print("=" * 50)

    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "solved", "steps", "runtime_ms"])

        for trial in range(1, args.trials + 1):
            board = Board.random()
            
            if args.show_progress and trial % 20 == 0:
                print(f"Progress: {trial}/{args.trials}")
            
            for name, solver in [("hill_climbing", hill_climbing), ("min_conflicts", min_conflicts)]:
                test_board = board.copy()
                start = time.perf_counter()
                solved, steps = solver.solve(test_board)
                runtime = (time.perf_counter() - start) * 1000
                
                writer.writerow([name, int(solved), steps, f"{runtime:.3f}"])

                if name == "min_conflicts" and solved and saved_samples < 3:
                    saved_samples += 1
                    with open(f"samples/solved_{saved_samples}.txt", "w") as sf:
                        sf.write(f"State: {test_board}\n")
                        sf.write(f"Conflicts: {test_board.heuristic()} (valid solution)\n\n")
                        sf.write("Board visualization:\n")
                        sf.write(test_board.display())
                        sf.write("\n")
                
                if name == "min_conflicts" and solved and displayed_samples < 3 and args.show_progress:
                    displayed_samples += 1
                    print(f"\nSolution #{displayed_samples}:")
                    print(f"State: {test_board}, Steps: {steps}, Time: {runtime:.3f}ms")
                    print(test_board.display())
                    print("-" * 30)

    print(f"\nComplete. Results in results.csv, {saved_samples} samples saved.")

if __name__ == "__main__":
    main() 