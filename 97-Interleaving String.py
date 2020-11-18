class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        # Initialize dp
        dp = [[False]*(n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        
        # Solve dp
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 and j == 0: continue
                c1 = (i > 0 and s1[i-1] == s3[i + j - 1])
                c2 = (j > 0 and s2[j-1] == s3[i + j - 1])
                print(c1, c2)
                dp[i][j] = (dp[i-1][j] and c1) or (dp[i][j - 1] and c2)
        #print(dp)
        return dp[-1][-1]