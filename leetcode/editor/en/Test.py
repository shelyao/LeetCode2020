from collections import deque, defaultdict
from heapq import *
class Solution:
    def maxResult(self, nums, k: int) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0]*n
        dp[-1] = nums[-1]
        heap = []
        heappush(heap, (-nums[-1], n-1))
        for i in range(n-2, -1, -1):
            while heap and heap[0][1] > i + k:
                heappop(heap)
            dp[i] += -heap[0][0] + nums[i]
            heappush(heap, (-dp[i], i))
        print(dp[0])
        return dp[0]
sol = Solution()
sol.maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2)