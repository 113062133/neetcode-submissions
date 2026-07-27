class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        n = len(digits)
        res = []
        cur = []

        m = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def dfs(i):
            if i == n:
                res.append("".join(cur))
                return

            for j in m[digits[i]]:
                cur.append(j)
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res