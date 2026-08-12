class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        top_row = 1
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        top_row = 0
                    if c == 0:
                        matrix[0][0] = 0
                    if r != 0 and c != 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0

        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        if top_row == 0:
            for c in range(n):
                matrix[0][c] = 0
        