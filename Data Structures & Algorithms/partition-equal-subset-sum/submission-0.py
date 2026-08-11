class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        m = {}
        n = len(nums)

        def dfs(i, cur):
            if cur == target:
                return True
            if i >= n:
                return False
            if (i, cur) in m:
                return m[(i, cur)]

            if cur + nums[i] <= target:
                m[(i, cur)] = dfs(i + 1, cur + nums[i]) or dfs(i+1, cur)
            else:
                m[(i, cur)] = dfs(i + 1, cur)
            return m[(i, cur)]

        return dfs(0, 0)