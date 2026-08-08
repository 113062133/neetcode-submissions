class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]
        
        n = len(nums1)
        m1 = {}
        m2 = {}

        def dfs1(i):
            if i >= n:
                return 0
            if i in m1:
                return m1[i]
            m1[i] = max(nums1[i] + dfs1(i + 2), dfs1(i + 1))
            return m1[i]

        def dfs2(i):
            if i >= n:
                return 0
            if i in m2:
                return m2[i]
            m2[i] = max(nums2[i] + dfs2(i + 2), dfs2(i + 1))
            return m2[i]
        
        return max(dfs1(0), dfs2(0))