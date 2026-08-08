class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        m = {}

        def dfs(i):
            if i >= n:
                return 1
            if s[i] == '0':
                return 0
            if i in m:
                return m[i]

            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                m[i] = dfs(i + 1) + dfs(i + 2)
            else:
                m[i] = dfs(i + 1)
            return m[i]

        return dfs(0)