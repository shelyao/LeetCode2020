class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for amt in range(1, amount+1):
            for coin in coins:
                if amt < coin: continue
                dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
    
    #dfs
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0: return 0
        if not coins: return -1
        memo = {}
        
        def dfs(amount):
            if amount == 0: return 0
            if amount < 0: return float('inf')
            
            if amount not in memo:
                res = float('inf')
                for coin in coins:
                    res = min(res, dfs(amount - coin) + 1)
                memo[amount] = res
            return memo[amount]
        
        ans = dfs(amount) 
        return ans if ans != float('inf') else -1