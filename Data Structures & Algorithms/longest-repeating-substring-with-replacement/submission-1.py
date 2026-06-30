class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        win_char = {}
        max_length = 0

        for right in range(len(s)):
            win_char[s[right]] = win_char.get(s[right], 0) + 1
            length = right - left + 1
            freq = max(win_char.values())
            replace = length - freq
            if replace <= k:
                max_length = max(length, max_length)
            else:
                win_char[s[left]] -= 1
                left += 1
        return max_length
        
            
