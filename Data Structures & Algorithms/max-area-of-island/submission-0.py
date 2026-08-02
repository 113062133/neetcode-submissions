class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxArea = 0

        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return 0

            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0

            area = 1
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row + 1, col)
            area += dfs(row, col - 1)

            return area

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    maxArea = max(area, maxArea)

        return maxArea