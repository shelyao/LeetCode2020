class Solution:
    def canPartition0(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False
        target = total//2
        
        dp = [False]*(target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target]
    
    #dfs
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False
        target = total//2
        memo = {}
        
        def dfs(nums, i, target):
            if target == 0: return True
            if len(nums) == 0 or target < 0:
                return False
            if (i, target) not in memo:
                memo[(i, target)] = dfs(nums[1:], i+1, target) or dfs(nums[1:], i+1, target - nums[0])
            return memo[(i, target)]
        return dfs(nums, 0, target)