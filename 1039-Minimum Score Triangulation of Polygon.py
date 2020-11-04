class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        A2 = A + A
        dp = [[0]*n*2 for _ in range(2*n)]
        for i in range(2*n, -1, -1):
            for j in range(i + 2, n*2):
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A2[i]*A2[j]*A2[k])
        return dp[0][n-1]