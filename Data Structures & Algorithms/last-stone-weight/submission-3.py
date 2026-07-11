class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            diff = abs(stone1 - stone2)
            if diff:
                heapq.heappush(heap, -diff)
        
        if heap:
            return -heap[0]
        else:
            return 0