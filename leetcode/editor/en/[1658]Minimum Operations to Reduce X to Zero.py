# You are given an integer array nums and an integer x. In one operation, you ca
# n either remove the leftmost or the rightmost element from the array nums and su
# btract its value from x. Note that this modifies the array for future operations
# . 
# 
#  Return the minimum number of operations to reduce x to exactly 0 if it's poss
# ible, otherwise, return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce
#  x to zero.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the
#  first two elements (5 operations in total) to reduce x to zero.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 104 
#  1 <= x <= 109 
#  
#  Related Topics Two Pointers Binary Search Greedy Sliding Window 
#  👍 905 👎 19


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        to_keep = total - x
        prefixSum = [0]
        idx_map = {0:-1}
        res, n = -1, len(nums)
        for i, num in enumerate(nums):
            pre = prefixSum[-1] + num
            prefixSum.append(pre)
            idx_map[pre] = i
            if pre >= to_keep and pre - to_keep in idx_map:
                start = idx_map[pre - to_keep]
                res = max(res, i - start)
        return n - res if res != -1 else -1

# leetcode submit region end(Prohibit modification and deletion)
