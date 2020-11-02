class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        n = len(nums)
        if len(nums) <= 2: return max(nums)
        
        dp = [0]*n
        res = 0
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            res = max(res, dp[i])
        
        return res