class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = {}
        n = len(nums)

        def dfs(i, j):
            if i >= n:
                return 0
            if (i, j) in m:
                return m[(i, j)]
            
            if j == -1 or nums[i] > nums[j]:
                m[(i, j)] = max(1 + dfs(i + 1, i), dfs(i + 1, j))
            else:
                m[(i, j)] = dfs(i + 1, j)
            return m[(i, j)]
            
        return dfs(0, -1)