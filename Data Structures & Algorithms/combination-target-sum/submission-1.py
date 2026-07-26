class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        n = len(nums)

        def dfs(i, s):
            if s == target:
                res.append(combination.copy())
                return
                
            if s > target or i == n:
                return

            combination.append(nums[i])
            dfs(i, s + nums[i])
            combination.pop()
            dfs(i + 1, s)

        dfs(0, 0)
        return res