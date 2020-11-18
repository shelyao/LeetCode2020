from functools import lru_cache
class Solution:
    # Top down
    def minDistance0(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0 or n == 0: return m + n
        
        dp = [[0]*(n+1) for _ in range(m + 1)]

        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j]+1, dp[i][j-1]+1)
        
        return dp[-1][-1]    
    # buttom up
    def minDistance1(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @lru_cache(None)
        def helper(i, j):
            if i < 0 or j < 0: return (i+j+2)
            if word1[i] == word2[j]:
                return helper(i-1, j-1)
            else:
                return 1 + min(helper(i-1, j-1), helper(i-1,j), helper(i,j-1))
        
        return helper(m-1, n-1) 
    # memo
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}
        
        def helper(i, j):
            if i < 0 or j < 0: return (i+j+2)
            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    res = helper(i-1, j-1)
                else:
                    res = 1 + min(helper(i-1, j-1), helper(i-1,j), helper(i,j-1))
                memo[(i, j)] = res
            return memo[(i,j)]
        
        return helper(m-1, n-1)
        