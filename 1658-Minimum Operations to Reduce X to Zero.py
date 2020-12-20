class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if not nums or len(nums) == 0 or x == 0: return 0
        target, n = sum(nums) - x, len(nums)
        left = PrefixSum = 0
        res = float('-inf')
        for right in range(n):
            PrefixSum += nums[right]
            while left <= right and PrefixSum > target:
                PrefixSum -= nums[left]
                left += 1
            if PrefixSum == target: res = max(res, right - left + 1)
        return -1 if res == float('-inf') else n - res