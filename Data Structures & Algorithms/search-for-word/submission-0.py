class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        n = len(board)
        m = len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True

            if row < 0 or row >= n or col < 0 or col >= m:
                return False
            if (row, col) in vis:
                return False    
            if board[row][col] != word[i]:
                return False

            vis.add((row, col))
            flag = dfs(row - 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row + 1, col, i + 1) or dfs(row, col - 1, i + 1)
            vis.remove((row, col))
            return flag

        for row in range(n):
            for col in range(m):
                if dfs(row, col, 0):
                    return True
        return False

                    