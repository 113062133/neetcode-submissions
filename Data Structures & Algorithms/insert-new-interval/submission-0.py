class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newstart = newInterval[0]
        newend = newInterval[1]
        res = []
        flag = 0

        for interval in intervals:
            if flag == 1:
                res.append(interval)
                continue

            start = interval[0]
            end = interval[1]

            if end < newstart:
                res.append(interval)
            elif newend >= start:
                newstart = min(newstart, start)
                newend = max(newend, end)
            elif newend < start:
                res.append([newstart, newend])
                res.append(interval)
                flag = 1

        if flag == 0:
            res.append([newstart, newend])

        return res