class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        if len(edges) != n - 1:
            return False

        graph = {}
        for node in range(n):
            graph[node] = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n