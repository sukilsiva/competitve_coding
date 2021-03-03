"""
Method1 1:
graph = {}
graph["A"] = {}
graph['A']['B'] = 2
graph['A']['C'] = 5

graph["B"] = {}
graph["B"]["C"] = 2
graph["B"]["D"] = 3

graph["C"] = {}
graph["C"]["D"] = 3

graph["D"] = {}

print(graph)"""

# Method 2
from collections import defaultdict
graph = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    u, v, w = map(str, input().split())
    graph[u].append((v, int(w)))
print(graph)