class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):
            if start == len(s):
                res.append(sub.copy())
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    sub.append(s[start:end + 1])
                    dfs(end + 1)
                    sub.pop()

        dfs(0)
        return res