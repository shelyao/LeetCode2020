class Solution:
    def minimumMoves(self, arr) -> int:
        if not arr or len(arr) == 0: return 0
        n = len(arr)
        if n == 1: return 1
        dp = [[n]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                if j >= n: continue 
                if arr[i] == arr[j]:
                    if j == i + 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                for p in range(i, j):
                    dp[i][j] = min(dp[i][p] + dp[p+1][j], dp[i][j])
        
        #print(dp)
        return dp[0][-1]