class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        step = 0

        while r < n - 1:
            step += 1
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest

        return step