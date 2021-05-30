# You are given a 0-indexed integer array nums and an integer k. 
# 
#  You are initially standing at index 0. In one move, you can jump at most k st
# eps forward without going outside the boundaries of the array. That is, you can 
# jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive
# . 
# 
#  You want to reach the last index of the array (index n - 1). Your score is th
# e sum of all nums[j] for each index j you visited in the array. 
# 
#  Return the maximum score you can get. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (und
# erlined above). The sum is 7.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3] (under
# lined above). The sum is 17.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length, k <= 105 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics Dequeue 
#  👍 410 👎 24


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0]*n
        dp[-1] = nums[-1]
        heap = []
        heappush(heap, (-nums[-1], n-1))
        for i in range(n-2, -1, -1):
            while heap and heap[0][1] > i + k:
                heappop(heap)
            dp[i] += -heap[0][0] + nums[i]
            heappush(heap, (-dp[i], i))
        return dp[0]



# leetcode submit region end(Prohibit modification and deletion)
