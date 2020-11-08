class Solution:
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        # top down
        @functools.lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            if i == j - 1:
                return arr[i]*arr[j]
            return min(max(arr[i:k])*max(arr[k:j + 1]) 
                       + dp(i, k-1) + dp(k, j) for k in range(i + 1, j + 1))
        
        return dp(0, len(arr) - 1)
    
    # bottom up
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr or len(arr) < 2: return 0
        n = len(arr)
        # init dp
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n - 1):
            dp[i][i] = 0
            dp[i][i + 1] = arr[i]*arr[i + 1]
        dp[-1][-1] = 0
        
        for i in range(n):
            for j in range(i - 2, -1, -1):
                for k in range(j + 1, i + 1):
                    dp[j][i] = min(dp[j][i], 
                                   max(arr[j:k])*max(arr[k:i + 1]) 
                                   + dp[j][k - 1] + dp[k][i])
        return dp[0][-1]
                