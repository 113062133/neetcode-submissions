class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {}
        child = {}

        for node in range(numCourses):
            indegree[node] = 0
            child[node] = []
        for a, b in prerequisites:
            indegree[a] += 1
            child[b].append(a)

        res = []
        q = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        while q:
            node = q.popleft()
            for c in child[node]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            res.append(node)

        if len(res) != numCourses:
            return []
        else:
            return res