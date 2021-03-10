class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x: (x[0], -x[1]))
        prev = intervals[0]
        res = 1
        for i in range(1, n):
            current = intervals[i]
            if current[1] <= prev[1]:
                continue
            prev = current
            res += 1
        return res