"""
A graph is a tree if it meets at least 2 of the 3 defs (2 => 3rd)
    - 1 connected component (i.e given any start node, all other nodes are reacheable)
    - n - 1 edges
    - No cycles ie. we do not revist nodes during dfs
"""
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        validEdgeCount = len(edges) == n - 1

        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        stack = [0]
        seen = {0}
        while stack:
            node = stack.pop()
            for neigh in graph[node]:
                if neigh != node and neigh not in seen:
                    seen.add(neigh)
                    stack.append(neigh)
        oneCC = len(seen) == n

        return oneCC and validEdgeCount