class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        prefix[1] = nums[0]
        for i in range(2, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        suffix = [1] * (n + 1)
        suffix[n-2] = nums[n-1]
        for i in range(n-3, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        output = []
        for i in range(n):
            output.append(prefix[i] * suffix[i])
        return output