class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        left = right = 0
        win_char = set()
        win_char.add(s[0])
        max_length = 1

        while right <= len(s) - 2:
            right += 1
            c = s[right]
            if c in win_char:
                while c in win_char:
                    win_char.remove(s[left])
                    left += 1
            win_char.add(c)
            length = right - left + 1
            max_length = max(length, max_length)
        return max_length