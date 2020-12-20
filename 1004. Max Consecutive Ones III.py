class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = res = zeros = 0
        N = len(A)
        for right in range(N):
            if A[right] == 0: zeros += 1
            while left < N and zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            #print(right, left, res, zeros)
        return res