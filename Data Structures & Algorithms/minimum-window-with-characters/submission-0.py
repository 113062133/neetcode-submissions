class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res = ""
        cnt1 = [0] * 128
        cnt2 = [0] * 128

        for c in t:
            cnt2[ord(c)] += 1

        def valid() -> bool:
            for i in range(128):
                if cnt1[i] < cnt2[i]:
                    return False
            return True

        left = 0
        for right in range(len(s)):
            cnt1[ord(s[right])] += 1
            while valid():
                sub = s[left: right + 1]
                if res == "" or len(sub) < len(res):
                    res = sub
                cnt1[ord(s[left])] -= 1
                left += 1
        return res
