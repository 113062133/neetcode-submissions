class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []
        n = len(candidates)

        def dfs(i, s):
            if s == target:
                res.append(combination.copy())
                return

            if s > target or i == n:
                return

            next_i = i + 1
            while next_i < n and candidates[next_i] == candidates[i]:
                next_i += 1

            combination.append(candidates[i])
            dfs(i + 1, s + candidates[i])
            combination.pop()
            dfs(next_i, s)

        dfs(0, 0)
        return res