import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        left = 0
        ans = []
        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            if right >= k - 1:
                ans.append(-heap[0][0])
                left += 1
                while heap and heap[0][1] < left:
                    heapq.heappop(heap)
        return ans