class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c.isalnum():
                t += c.lower()
        
        n = len(t)
        for i in range(n // 2):
            if t[i] != t[n - 1 - i]:
                return False
        return True