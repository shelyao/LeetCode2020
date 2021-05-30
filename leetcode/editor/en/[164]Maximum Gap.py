# Given an integer array nums, return the maximum difference between two success
# ive elements in its sorted form. If the array contains less than two elements, r
# eturn 0. 
# 
#  You must write an algorithm that runs in linear time and uses linear extra sp
# ace. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) 
# has the maximum difference 3.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  0 <= nums[i] <= 109 
#  
#  Related Topics Sort 
#  👍 1198 👎 220


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1: return 0
        heap = []
        res = 0
        for num in nums:
            heappush(heap, num)
        pre = heappop(heap)
        while heap:
            curr = heappop(heap)
            res = max(res, curr - pre)
            pre = curr
        return res
# leetcode submit region end(Prohibit modification and deletion)
