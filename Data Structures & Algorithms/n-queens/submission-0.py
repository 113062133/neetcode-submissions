class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = [['.'] * n for _ in range(n)]

        def valid(row, col):
            for i in range(row):
                if cur[i][col] == 'Q':
                    return False

            r = row - 1
            c = col - 1
            while r >= 0 and c >= 0:
                if cur[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r = row - 1
            c = col + 1
            while r >= 0 and c < n:
                if cur[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

            return True

        def dfs(row):
            if row == n:
                res.append([''.join(row) for row in cur])
                return
            
            for col in range(n):
                if valid(row, col):
                    cur[row][col] = 'Q'
                    dfs(row + 1)
                    cur[row][col] = '.'

        dfs(0)
        return res