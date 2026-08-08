class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        num = 0

        for i in range(n):
            num += 1

            k = 1
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                num += 1
                k += 1

            if i + 1 < n and s[i] == s[i + 1]:
                num += 1
                k = 1
                while i - k >= 0 and i + 1 + k < n and s[i - k] == s[i + 1 + k]:
                    num += 1
                    k += 1
            
        return num
        