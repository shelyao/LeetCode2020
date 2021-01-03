class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque([(nums[0], 0)])
        res = nums[0]
        for i in range(1, n):
            while dq and dq[0][1] < i - k:
                dq.popleft()
            current = nums[i] + max(0, dq[0][0])
            while dq and dq[-1][0] < current:
                dq.pop()
            res = max(res, current)
            dq.append((current, i))
        return res