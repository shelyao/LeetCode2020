class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if s <= 0 or s > sum(nums): return 0
        left = subSum = 0
        res = N = len(nums)
        for right in range(N):
            if s == nums[right]: return 1
            subSum += nums[right]
            while subSum >= s and right >= left:
                res = min(res, right - left + 1)
                subSum -= nums[left]
                left += 1
        return res
            