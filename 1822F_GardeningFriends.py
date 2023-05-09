from sys import stdin
from collections import defaultdict

def depth_first_search(graph, vertex, parent, depth):
    max_depth = depth
    max_vertex = vertex

    for neighbor in graph[vertex]:
        if neighbor != parent:
            sub_max_depth, sub_max_vertex = depth_first_search(graph, neighbor, vertex, depth + 1)
            if sub_max_depth > max_depth:
                max_depth = sub_max_depth
                max_vertex = sub_max_vertex

    return max_depth, max_vertex

def max_profit(t, test_cases):
    results = []

    for i in range(t):
        n, k, c, edges = test_cases[i]
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        max_depth, _ = depth_first_search(graph, 1, None, 0)

        if c >= k:
            results.append(max_depth * k)
        else:
            profit = (max_depth - 1) * k - c
            results.append(profit)

    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, k, c = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    test_cases.append((n, k, c, edges))

# Find maximum profit
profits = max_profit(t, test_cases)

# Print output
for profit in profits:
    print(profit)