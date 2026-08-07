class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parent[root1] = root2
            return True
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n + 1)
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]