class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            row, col = q.popleft()
            for i in range(4):
                nrow, ncol = row + dirs[i][0], col + dirs[i][1]
                if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m:
                    continue
                if grid[nrow][ncol] == 2147483647:
                    grid[nrow][ncol] = grid[row][col] + 1
                    q.append((nrow, ncol))