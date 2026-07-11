class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1

        time = 0
        heap = []
        q = deque()

        for task, freq in freqs.items():
            heapq.heappush(heap, (-freq, task))

        while heap or q:
            time += 1
            while q and q[0][2] <= time:
                freq, task, available_time = q.popleft()
                heapq.heappush(heap, (freq, task))
            
            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    q.append((freq, task, time + n + 1))
        return time