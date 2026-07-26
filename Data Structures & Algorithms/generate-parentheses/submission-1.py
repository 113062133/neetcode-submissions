class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []

        def dfs(left, right):
            if left == n and right == n:
                res.append("".join(string))
                return

            if left < n:
                string.append('(')
                dfs(left + 1, right)
                string.pop()

            if right < left:
                string.append(')')
                dfs(left, right + 1)
                string.pop()

        dfs(0, 0)
        return res