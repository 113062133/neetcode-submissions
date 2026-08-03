class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            row, col = q.popleft()
            for i in range(4):
                nrow, ncol = row + dir[i][0], col + dir[i][1]
                if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m:
                    continue
                if grid[nrow][ncol] == 2147483647:
                    grid[nrow][ncol] = 1 if grid[row][col] == -1 else grid[row][col] + 1
                    q.append((nrow, ncol))