class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1: return n
        points.sort()
        prev = points[0]
        res = 1
        for i in range(1, n):
            current = points[i]
            if current[0] > prev[1]:
                prev = current[:]
                res += 1
            else:
                left = max(prev[0], current[0])
                right = min(prev[1], current[1])
                prev = [left, right]
        return res