class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = {}

        def dfs(i):
            if i >= n:
                return True
            if i in m:
                return m[i]
            
            for word in wordDict:
                if i + len(word) <= n and s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        m[i] = True
                        return True            
            m[i] = False
            return False

        return dfs(0)