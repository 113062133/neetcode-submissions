class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        res = []
        pacific = set()
        atlantic = set()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def dfs(row, col, vis):
            if (row, col) in vis:
                return
            vis.add((row, col))

            for dr, dc in dirs:
                nrow, ncol = row + dr, col + dc
                if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m:
                    continue
                if heights[nrow][ncol] >= heights[row][col]:
                    dfs(nrow, ncol, vis)
        
        for row in range(n):
            for col in range(m):
                if row == 0 or col == 0:
                    dfs(row, col, pacific)
                if row == n - 1 or col == m - 1:
                    dfs(row, col, atlantic)

        for row in range(n):
            for col in range(m):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res