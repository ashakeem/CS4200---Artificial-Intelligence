# helper script to summarize results.csv (assisted with GPT)

import csv
from collections import defaultdict

costs = {'h1': defaultdict(list), 'h2': defaultdict(list)}

with open('results.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        h = row['heuristic']
        d = int(row['depth'])
        nodes = int(row['nodes'])
        if h in costs:
            costs[h][d].append(nodes)

print(f"{'d':>3} | {'A*(h1)':>8} | {'A*(h2)':>8}")
print('-'*30)
for d in sorted(set(costs['h1']) | set(costs['h2'])):
    avg_h1 = sum(costs['h1'][d])/len(costs['h1'][d]) if costs['h1'][d] else float('nan')
    avg_h2 = sum(costs['h2'][d])/len(costs['h2'][d]) if costs['h2'][d] else float('nan')
    print(f"{d:>3} | {avg_h1:>8.0f} | {avg_h2:>8.0f}") 