class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for node in range(numCourses):
            graph[node] = []
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node, path):
            if node in path:
                return False
            
            path.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor, path):
                    return False
            path.remove(node)
            graph[node].clear()
            return True
        
        for node in range(numCourses):
            path = set()
            if not dfs(node, path):
                return False
        return True