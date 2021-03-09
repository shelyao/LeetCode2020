class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []: return [newInterval]
        if newInterval == []: return intervals
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        start, n = 0, len(intervals)
        res = []
        addflag = 0
        while start < n:
            if intervals[start][0] > newInterval[1] or intervals[start][1] < newInterval[0]:
                res.append(intervals[start])
                start += 1
                continue
            while start < n and ((newInterval[0] <= intervals[start][1] <= newInterval[1]) or \
                                 (newInterval[0] <= intervals[start][0] <= newInterval[1]) or \
                                 (newInterval[0] <= intervals[start][0] and newInterval[1] >= intervals[start][1]) or \
                                 (newInterval[0] >= intervals[start][0] and newInterval[1] <= intervals[start][1])):
                left = min(newInterval[0], intervals[start][0])
                right = max(newInterval[1], intervals[start][1])
                newInterval = [left, right]
                start += 1
            res.append(newInterval)
            addflag = 1
        
        if not addflag: res.append(newInterval)
        return sorted(res)