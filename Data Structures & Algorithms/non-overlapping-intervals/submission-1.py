class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        cnt = 0

        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]

            if start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                cnt += 1
                
        return cnt