class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range (0, len(nums)):
            diff = target - nums[i]
            if diff in m:
                return [m[diff], i]
            else:
                m[nums[i]] = i
