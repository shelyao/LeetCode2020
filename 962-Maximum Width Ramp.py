class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        n = len(A)
        res = 0
        for i in range(n):
            if not stack or A[i] < A[stack[-1]]:
                stack.append(i)
        
        for i in range(n-1, -1, -1):
            while stack and A[i] >= A[stack[-1]]:
                res = max(res, i - stack.pop())
        return res