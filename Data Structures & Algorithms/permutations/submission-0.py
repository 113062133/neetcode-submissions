class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        n = len(nums)
        arr = [False] * n

        def dfs():
            if len(temp) == n:
                res.append(temp.copy())
                return

            for i in range(n):
                if arr[i] == False:
                    temp.append(nums[i])
                    arr[i] = True
                    dfs()
                    temp.pop()
                    arr[i] = False

        dfs()
        return res