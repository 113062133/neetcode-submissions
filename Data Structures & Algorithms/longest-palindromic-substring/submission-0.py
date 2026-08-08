class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 1
        idx = 0

        for i in range(n):
            oddLen = 1
            oddIdx = i
            k = 1
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                oddLen += 2
                oddIdx -= 1
                k += 1

            if oddLen > maxLen:
                maxLen = oddLen
                idx = oddIdx

            if i + 1 < n and s[i] == s[i + 1]:
                evenLen = 2
                evenIdx = i
                k = 1
                while i - k >= 0 and i + 1 + k < n and s[i - k] == s[i + 1 + k]:
                    evenLen += 2
                    evenIdx -= 1
                    k += 1

                if evenLen > maxLen:
                    maxLen = evenLen
                    idx = evenIdx
            
        return s[idx:idx + maxLen]

            