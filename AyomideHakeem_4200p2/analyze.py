#analyze.py helper aided with Gen AI to analyze the results of the benchmark.py file
import csv, os

def analyze_results(csv_file="results.csv"):
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found. Run 'python3 benchmark.py' first.")
        return
    
    data = {"hill_climbing": [], "min_conflicts": []}
    
    with open(csv_file) as f:
        for row in csv.DictReader(f):
            if row["algorithm"] in data:
                data[row["algorithm"]].append({
                    "solved": int(row["solved"]),
                    "steps": int(row["steps"]),
                    "runtime": float(row["runtime_ms"])
                })
    
    print("\n" + "="*50)
    print("8-QUEEN SOLVER ANALYSIS")
    print("="*50)
    
    for algo, results in data.items():
        if not results: continue
        
        solved = sum(r["solved"] for r in results)
        total = len(results)
        rate = (solved / total) * 100
        
        solved_only = [r for r in results if r["solved"]]
        avg_steps = sum(r["steps"] for r in solved_only) / len(solved_only) if solved_only else 0
        avg_time = sum(r["runtime"] for r in solved_only) / len(solved_only) if solved_only else 0
        
        print(f"\n{algo.upper().replace('_', ' ')}")
        print(f"  Success Rate: {solved}/{total} = {rate:.1f}%")
        if solved_only:
            print(f"  Avg Steps (solved): {avg_steps:.1f}")
            print(f"  Avg Runtime (solved): {avg_time:.3f}ms")
    
    print("\nSAMPLE SOLUTIONS:")
    if os.path.exists("samples"):
        files = sorted([f for f in os.listdir("samples") if f.startswith("solved_")])
        print(f"  Found {len(files)} valid solutions in samples/")
        print("  (Full board visualizations available in sample files)")
    
    print("="*50)

if __name__ == "__main__":
    analyze_results() 