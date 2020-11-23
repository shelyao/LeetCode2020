class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for amt in range(1, amount + 1):
                if amt >= coin:
                    dp[amt] += dp[amt - coin]
        
        return dp[-1]