class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        left = 0
        res = float('-inf')
        n = len(points)
        stack = deque()
        for right, p in enumerate(points):
            while stack and p[0] - stack[0][1] > k:
                stack.popleft()
            while stack and stack[-1][0] < p[1] - p[0]:
                val, x, y = stack.pop()
                res = max(res, p[0] + p[1] + val)
            stack.append([p[1] - p[0], p[0], p[1]])
            if len(stack) > 1:
                res = max(res, p[0] + p[1] + stack[0][0])
        return res