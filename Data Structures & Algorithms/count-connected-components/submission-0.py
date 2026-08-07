class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.parent[root1] = root2
            return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num = n
        dsu = DSU(n)
        for a, b in edges:
            if dsu.union(a, b):
                num -= 1
        return num