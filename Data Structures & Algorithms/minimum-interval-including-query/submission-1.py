class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        qi = []
        for i, q in enumerate(queries):
            qi.append([q, i])
        qi.sort()

        output = [-1] * len(queries)
        heap = []
        j = 0

        for q, i in qi:
            while j < len(intervals):
                start, end = intervals[j]
                if start <= q:
                    size = end - start + 1
                    heapq.heappush(heap, [size, end])
                    j += 1
                else:
                    break
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                output[i] = heap[0][0]
        
        return output