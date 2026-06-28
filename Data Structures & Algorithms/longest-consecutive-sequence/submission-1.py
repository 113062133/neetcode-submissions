class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0
        for num in s:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                max_length = max(length, max_length)
        return max_length