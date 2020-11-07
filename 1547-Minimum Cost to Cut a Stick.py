class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        if not cuts or len(cuts) == 0: return 0
    
        arr = [0] + sorted(cuts) + [n]
        n = len(arr)
        dp = [[0] *n for _ in range(n)]
        
        for l in range(n-3, -1, -1):
            for r in range(l+2, n):
                dp[l][r] = min([dp[l][i] + dp[i][r] for i in range(l+1,r)])
                dp[l][r] += arr[r] - arr[l]
        
        return dp[0][-1]