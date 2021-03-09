class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        if intervals == [[]] or toBeRemoved == []: return intervals
        start, n = 0, len(intervals)
        res = []
        for start in range(n):
            interval = intervals[start]
            if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
                res.append(interval)
            elif toBeRemoved[0] < interval[0] and toBeRemoved[1] >= interval[1]:
                continue
            elif interval[0] < toBeRemoved[0] <= interval[1] and interval[0] <= toBeRemoved[1] < interval[1]:
                int1 = [interval[0], toBeRemoved[0]]
                int2 = [toBeRemoved[1], interval[1]]
                res.append(int1)
                res.append(int2)
            else:
                if interval[0] < toBeRemoved[0] <= interval[1]:
                    res.append([interval[0], toBeRemoved[0]])
                if interval[1] > toBeRemoved[1] >= interval[0]:
                    res.append([toBeRemoved[1], interval[1]])
        return res
                
            