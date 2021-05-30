# Given an array of non-negative integers nums, you are initially positioned at 
# the first index of the array. 
# 
#  Each element in the array represents your maximum jump length at that positio
# n. 
# 
#  Determine if you are able to reach the last index. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jum
# p length is 0, which makes it impossible to reach the last index.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  0 <= nums[i] <= 105 
#  
#  Related Topics Array Greedy 
#  👍 6487 👎 427


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if nums[0] == 0: return False
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1, n-1):
            dp[i] = max(dp[i-1]-1, nums[i])
            if dp[i] == 0: return False

        return True
# leetcode submit region end(Prohibit modification and deletion)
