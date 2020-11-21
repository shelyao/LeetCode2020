class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0: return 0
        
        dp = [[float('-inf')]*n for _ in range(m)]
        dp[0][0] = nums1[0]*nums2[0]
        for i in range(1, m):
            dp[i][0] = max(dp[i-1][0], nums1[i]*nums2[0])
        
        for j in range(1, n):
            dp[0][j] = max(dp[0][j-1], nums1[0]*nums2[j])
        
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i]*nums2[j] > 0:
                    dp[i][j] = max(dp[i-1][j-1] + nums1[i]*nums2[j], dp[i][j-1], dp[i-1][j], nums1[i]*nums2[j])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    
        return dp[-1][-1]