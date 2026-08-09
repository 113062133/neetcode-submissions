class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = 1
        min_p = 1
        res_p = -float("inf")

        for num in nums:
            old_max_p = max_p
            old_min_p = min_p
            max_p = max(num, old_max_p * num, old_min_p * num)
            min_p = min(num, old_max_p * num, old_min_p * num)
            res_p = max(res_p, max_p)
        return res_p