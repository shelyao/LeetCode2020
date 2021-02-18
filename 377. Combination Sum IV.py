class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(maxsize = None)
        def dfs(total):
            if total == target:
                return 1
            res = 0
            for i in range(len(nums)):
                if total + nums[i] <= target:
                    res += dfs(total + nums[i])
            return res
        return dfs(0)
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[-1]