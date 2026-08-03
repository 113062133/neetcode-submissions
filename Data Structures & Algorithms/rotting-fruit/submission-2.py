class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        flag = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] != 0:
                    flag = 1
        if not flag:
            return 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    q.append((row, col))

        level = -1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nrow, ncol = row + dr, col + dc
                    if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m:
                        continue
                    if grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        q.append((nrow, ncol))
            level += 1
            
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    return -1
        return level