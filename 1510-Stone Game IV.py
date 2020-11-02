class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        ## idea: dp[n] = any(dp[n - i*i] == False)
        ## dp[0] = 0
        dp = [0]*(n+1)
        dp[1] = 1
        square = [i*i for i in range(1, int(n**0.5) + 1) if i*i <= n]
        for i in range(n+1):
            if dp[i] == 1: continue
            for j in square:
                if i + j > n: break
                else: dp[i + j] = 1
        return dp[-1]