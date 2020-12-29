class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res, deq = [0]*n, deque([0])
        res[0] = nums[0]
        for i in range(1, n):
            while deq and deq[0] < i - k:
                deq.popleft()
            res[i] = res[deq[0]] + nums[i]
            while deq and res[i] >= res[deq[-1]]:
                deq.pop()
            deq.append(i)
        return res[-1]
        