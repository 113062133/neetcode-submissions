from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        left = 0
        ans = []

        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if q[0] <= right - k:
                q.popleft()
            if right >= k - 1:
                ans.append(nums[q[0]])
        return ans