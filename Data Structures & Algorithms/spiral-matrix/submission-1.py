class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()

        r = c = idx = 0
        while len(res) < m * n:
            res.append(matrix[r][c])
            vis.add((r, c))
            nr, nc = r + dirs[idx][0], c + dirs[idx][1]
            if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in vis:
                idx = 0 if idx == 3 else idx + 1
                nr, nc = r + dirs[idx][0], c + dirs[idx][1]
            r, c = nr, nc
        
        return res