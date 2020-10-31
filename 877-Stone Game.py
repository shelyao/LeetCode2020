class Solution:
    ## Math
    def stoneGame1(self, piles: List[int]) -> bool:
        return True
    
    ## recursion
    def stoneGame2(self, piles: List[int]) -> bool:
        N = len(piles)
        memo = [[float('-inf')]*N for _ in range(N)]
        
        def dp(l, r, memo):
            if l == r: return piles[l]
            if memo[l][r] == float('-inf'):
                memo[l][r] = max(piles[l] - dp(l+1, r, memo),
                                piles[r] - dp(l, r-1, memo))
            return memo[l][r]

        return dp(0, N-1, memo) > 0
    
    ## Iterative dp
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        #dp[i][j] : max(Alex-Lee) for pile i to pile j
        dp = [[0]*N for _ in range(N)]
        for i in range(N):
            dp[i][i] = piles[i]
            
        for size in range(2, N+1):
            for i in range(N - size + 1):
                j = i + size - 1
                dp[i][j] = max(piles[i] - dp[i+1][j],
                              piles[j] - dp[i][j-1])
        return dp[0][N-1] > 0