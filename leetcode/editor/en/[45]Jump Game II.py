# Given an array of non-negative integers nums, you are initially positioned at 
# the first index of the array. 
# 
#  Each element in the array represents your maximum jump length at that positio
# n. 
# 
#  Your goal is to reach the last index in the minimum number of jumps. 
# 
#  You can assume that you can always reach the last index. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 
# step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,3,0,1,4]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics Array Greedy 
#  👍 4486 👎 192


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        max_pos = max_steps = nums[0]
        res = 1
        for i, num in enumerate(nums):
            if max_steps < i:
                max_steps = max_pos
                res += 1
            max_pos = max(max_pos, i+num)
        return res
# leetcode submit region end(Prohibit modification and deletion)
