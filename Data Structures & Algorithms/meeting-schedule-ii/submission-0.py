"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        s = 0
        e = 0
        cnt = 0
        max_cnt = 0

        while s < len(start):
            if start[s] < end[e]:
                s += 1
                cnt += 1
            else:
                e += 1
                cnt -= 1
            max_cnt = max(max_cnt, cnt)

        return max_cnt