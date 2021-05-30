# Given an integer array nums, you need to find one continuous subarray that if 
# you only sort this subarray in ascending order, then the whole array will be sor
# ted in ascending order. 
# 
#  Return the shortest such subarray and output its length. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the 
# whole array sorted in ascending order.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# Follow up: Can you solve it in O(n) time complexity? Related Topics Array 
#  👍 3939 👎 179


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1: return 0
        left, right = n-1, 0
        temp_max = nums[0]
        temp_min = nums[-1]
        for i, x in enumerate(nums):
            temp_max = max(temp_max, x)
            if x < temp_max:
                right = i
        for i, x in enumerate(nums[::-1]):
            temp_min = min(temp_min, x)
            if x > temp_min:
                left = n-i-1
        if right == 0: return 0
        return right - left + 1
# leetcode submit region end(Prohibit modification and deletion)
