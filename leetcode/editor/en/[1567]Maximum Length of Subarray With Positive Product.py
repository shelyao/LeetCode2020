# Given an array of integers nums, find the maximum length of a subarray where t
# he product of all its elements is positive. 
# 
#  A subarray of an array is a consecutive sequence of zero or more values taken
#  out of that array. 
# 
#  Return the maximum length of a subarray with positive product. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which has
#  a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the product
#  0 which is not positive. 
# 
#  Example 3: 
# 
#  
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
# 
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [-1,2]
# Output: 1
#  
# 
#  Example 5: 
# 
#  
# Input: nums = [1,2,3,5,-6,4,0,10]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^9 <= nums[i] <= 10^9 
#  
#  Related Topics Greedy 
#  👍 419 👎 7


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if list(set(nums)) == [0]: return 0
        res = 0
        n = len(nums)
        negative = []
        start, sign = 0, 1
        for i in range(n):
            if sign == 1:
                res = max(res, i - start)
            if nums[i] < 0:
                sign *= -1
                negative.append(i)
            if nums[i] == 0:
                if sign == 1:
                    res = max(res, i - start)
                else:
                    if len(negative) == 1:
                        neg_idx = negative[0]
                        res = max(res, neg_idx - start, i - neg_idx - 1)
                    else:
                        neg_idx0, neg_idx1 = negative[0], negative[-1]
                        res = max(res, i - neg_idx0 - 1, neg_idx1-start)
                negative = []
                start, sign = i + 1, 1
            if i == n - 1:
                if sign == 1:
                    res = max(res, i - start + 1)
                else:
                    if len(negative) == 1:
                        neg_idx = negative[0]
                        res = max(res, neg_idx - start, i - neg_idx)
                    else:
                        neg_idx0, neg_idx1 = negative[0], negative[-1]
                        res = max(res, i - neg_idx0, neg_idx1-start)
        return res
# leetcode submit region end(Prohibit modification and deletion)
