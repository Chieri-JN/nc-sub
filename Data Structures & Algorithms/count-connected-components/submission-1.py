class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ccCount = 0
        seen = set()

        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        for node in graph:
            if node not in seen:
                ccCount += 1
                seen.add(node)
                stack = [node]
                while stack:
                    v = stack.pop()
                    for nh in graph[v]:
                        if nh != v and nh not in seen:
                            seen.add(nh)
                            stack.append(nh)

        for i in range(n):
            if i not in seen:
                ccCount += 1

        return ccCount