class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            newstart = newInterval[0]
            newend = newInterval[1]

            if end < newstart:
                res.append(interval)
            elif newend >= start:
                newInterval = [min(newstart, start), max(newend, end)]
            elif newend < start:
                res.append(newInterval)
                return res + intervals[i:]

        res.append(newInterval)
        return res