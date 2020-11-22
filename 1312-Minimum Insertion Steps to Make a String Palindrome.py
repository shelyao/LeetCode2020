class Solution:
    def minInsertions0(self, s: str) -> int:
        if not s or len(s) == 1: return 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i+1][j-1] + 2, dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return n - dp[0][-1]
    
    # dfs  -- much slower
    def minInsertions(self, s: str) -> int:
        if not s or len(s) == 1: return 0
        n = len(s)
        memo = {}
        
        def dfs(i, j):
            if i == j: return 1
            if i > j: return 0
            if (i, j) not in memo:
                if s[i] == s[j]:
                    res = max(dfs(i+1, j-1) + 2, dfs(i+1, j), dfs(i, j-1))
                else:
                    res = max(dfs(i+1, j), dfs(i, j-1))
                memo[(i, j)] = res
            
            return memo[(i, j)]
        return n - dfs(0, n-1)