class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        n = len(nums)

        def dfs(i):
            if i == n:
                res.append(subset.copy())
                return
            
            next_i = i + 1
            while next_i < n and nums[next_i] == nums[i]:
                next_i += 1

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(next_i)

        dfs(0)
        return res
        