class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        m = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in m:
                return m[i]
            m[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return m[i]
        
        return dfs(0)