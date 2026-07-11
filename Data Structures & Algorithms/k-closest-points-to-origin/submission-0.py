class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []

        for x, y in points:
            d = x**2 + y**2
            if len(heap) < k:
                heapq.heappush(heap, [-d, x, y])
            elif d < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [-d, x, y])

        for point in heap:
            x = point[1]
            y = point[2]
            ans.append([x, y])
        return ans