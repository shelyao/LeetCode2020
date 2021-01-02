class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0: return []
        if k == 1: return nums
        dq = deque(maxlen = k)
        max_idx = 0
        res = []
        for i in range(n):
            if dq and dq[0] == i - k: dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i < k and nums[i] > nums[max_idx]:
                max_idx = i
            if i < k-1: continue
            if i == k-1: res.append(nums[max_idx])
            else: res.append(nums[dq[0]])
        return res