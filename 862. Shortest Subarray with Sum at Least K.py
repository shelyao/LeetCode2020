class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefixSum = [0]
        for i in range(len(A)):
            prefixSum.append(prefixSum[-1] + A[i])
        res = len(A) + 1
        stack = deque()
        for right, num in enumerate(prefixSum):
            while stack and num <= prefixSum[stack[-1]]:
                stack.pop()
            while stack and num - prefixSum[stack[0]] >= K:
                res = min(res, right - stack.popleft())
            stack.append(right)
        return res if res != len(A) + 1 else -1