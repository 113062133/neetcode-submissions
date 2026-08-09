class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = {}

        def dfs(i):
            if i >= n:
                return True
            if i in m:
                return m[i]
            
            for j in range(i, n):
                for word in wordDict:
                    if s[i:j + 1] == word:
                        if dfs(j + 1):
                            m[i] = True
                            return True
            m[i] = False
            return False

        return dfs(0)