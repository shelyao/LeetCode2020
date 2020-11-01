class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        ## main idea: dp[i] = max(sum(s[i:i+k]) - dp[i+k]) for k in (1,2,3)
        n = len(stoneValue)
        stoneValue = stoneValue + [0, 0, 0]
        dp = [float('-inf') for _ in range(n)] + [0, 0, 0]
        for i in range(n - 1, -1, -1):
            for k in (1, 2, 3):
                dp[i] = max(dp[i], sum(stoneValue[i:i+k]) - dp[i+k])
        if dp[0] == 0: return "Tie"
        elif dp[0] > 0: return "Alice"
        else: return "Bob"