class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        
        intervals.sort(key = lambda x: (x[1], x[0]))
        end = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if interval[0] < end:
                res += 1
            else:
                end = interval[1]
        return res
            