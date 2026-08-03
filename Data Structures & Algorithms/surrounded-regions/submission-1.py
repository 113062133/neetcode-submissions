class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(row, col):
            board[row][col] = '#'
            for dr, dc in dirs:
                nrow, ncol = row + dr, col + dc
                if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m:
                    continue
                if board[nrow][ncol] == 'O':
                    dfs(nrow, ncol)

        for row in range(n):
            for col in range(m):
                if row == 0 or row == n - 1 or col == 0 or col == m - 1:
                    if board[row][col] == 'O':
                        dfs(row, col)

        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'