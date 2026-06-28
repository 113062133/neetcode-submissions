class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                c = board[i][j]
                if c == '.':
                    continue

                idx = (i // 3) * 3 + (j // 3)
                if c in rows[i] or c in cols[j] or c in boxes[idx]:
                    return False
                else:
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[idx].add(c)
        return True

