class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals.append([float('inf'), float('inf')])
        res = []
        i, n = 1, len(intervals)
        while i < n:
            current = intervals[i-1]
            while i < n and intervals[i][0] <= current[1]:
                current[1] = max(current[1], intervals[i][1])
                i += 1
            res.append(current)
            i += 1
        return res