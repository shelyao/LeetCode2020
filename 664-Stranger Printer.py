class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s or s == '': return 0
        n = len(s)
        self.dp = [[0]*n for _ in range(n)]
        return self.helper(s, 0, n - 1)
    
    def helper(self, s, l, r):
        if l > r: return 0
        if self.dp[l][r] > 0: return self.dp[l][r]
        
        res = self.helper(s, l, r - 1) + 1
        
        for k in range(l, r):
            if s[k] == s[r]:
                res = min(res, self.helper(s, l, k) + self.helper(s, k + 1, r - 1))
                
        self.dp[l][r] = res
        
        return self.dp[l][r]