class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if S > sum(nums): return 0
        memo = {}
        
        def dfs(nums, s, i):
            if nums == [] and s == 0: return 1
            if nums == [] and s != 0: return 0
            
            if (i, s) not in memo:
                res = 0
                res += dfs(nums[1:], s-nums[0], i+1)
                res += dfs(nums[1:], s+nums[0], i+1)
                memo[(i, s)] = res
            
            return memo[(i, s)]
        return dfs(nums, S, 0)
    # dp
    def findTargetSumWays(self, nums, S: int) -> int:
        #dp[i][s]: # of ways to make sum of nums[:i] to target s
        if S > sum(nums): return 0
        n = len(nums)
        
        dp = [[0]*2001 for _ in range(n)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        
        for i in range(1, n):
            for s in range(-1000, 1001):
                if dp[i-1][s+1000] > 0:
                    dp[i][s-nums[i] + 1000] += dp[i-1][s+1000]
                    dp[i][s+nums[i] + 1000] += dp[i-1][s+1000]
        return dp[-1][S+1000]