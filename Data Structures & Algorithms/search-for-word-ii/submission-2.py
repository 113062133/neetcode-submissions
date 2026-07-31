class TrieNode:
    def __init__(self):
        self.c = {}
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        n = len(board)
        m = len(board[0])
        root = TrieNode()

        for index, word in enumerate(words):
            l = len(word)
            cur = root
            for i in range(l):
                if word[i] not in cur.c:
                    cur.c[word[i]] = TrieNode()
                if i == l - 1:
                    cur.c[word[i]].is_end = True
                    cur.c[word[i]].index = index
                cur = cur.c[word[i]]

        def dfs(row, col, node):
            if row < 0 or row >= n or col < 0 or col >= m:
                return

            ch = board[row][col]
            if ch == '#' or ch not in node.c:
                return

            next_node = node.c[ch]
            if next_node.index != -1:
                res.append(words[next_node.index])
                next_node.index = -1

            board[row][col] = '#'

            dfs(row - 1, col, next_node)
            dfs(row, col + 1, next_node)
            dfs(row + 1, col, next_node)
            dfs(row, col - 1, next_node)

            board[row][col] = ch

        for row in range(n):
            for col in range(m):
                dfs(row, col, root)
        return res            