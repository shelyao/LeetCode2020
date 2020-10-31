class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = {}
        return self.helper(piles, 0, 1, dp)
        
    def helper(self, piles, start, M, dp):
        if start >= len(piles): return 0
        if len(piles) - start <= 2*M:
            return sum(piles[start:])
        if (start, M) in dp:
            return dp[(start, M)]
        
        my_score = 0
        total_score = sum(piles[start:])
        
        for x in range(1, 2*M+1):
            op_score = self.helper(piles, start + x, max(x, M), dp)
            my_score = max(my_score, total_score - op_score)
        
        dp[(start, M)] = my_score
        return my_score