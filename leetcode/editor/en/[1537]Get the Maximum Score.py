# You are given two sorted arrays of distinct integers nums1 and nums2. 
# 
#  A valid path is defined as follows: 
# 
#  
#  Choose array nums1 or nums2 to traverse (from index-0). 
#  Traverse the current array from left to right. 
#  If you are reading any value that is present in nums1 and nums2 you are allow
# ed to change your path to the other array. (Only one repeated value is considere
# d in the valid path). 
#  
# 
#  Score is defined as the sum of uniques values in a valid path. 
# 
#  Return the maximum score you can obtain of all possible valid paths. 
# 
#  Since the answer may be too large, return it modulo 10^9 + 7. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
# Output: 30
# Explanation: Valid paths:
# [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
# [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
# The maximum is obtained with the path in green [2,4,6,8,10].
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
# Output: 109
# Explanation: Maximum sum is obtained with the path [1,3,5,100].
#  
# 
#  Example 3: 
# 
#  
# Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
# Output: 40
# Explanation: There are no common elements between nums1 and nums2.
# Maximum sum is obtained with the path [6,7,8,9,10].
#  
# 
#  Example 4: 
# 
#  
# Input: nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
# Output: 61
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length <= 10^5 
#  1 <= nums2.length <= 10^5 
#  1 <= nums1[i], nums2[i] <= 10^7 
#  nums1 and nums2 are strictly increasing. 
#  
#  Related Topics Dynamic Programming 
#  👍 318 👎 22


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        duplicates = set(nums1) & set(nums2)
        if not duplicates:
            return max(sum(nums1), sum(nums2))
        p1, p2 = len(nums1) - 1, len(nums2) - 1
        current_max = 0
        while p1 >= 0 and p2 >= 0:
            sum1 = sum2 = 0
            while p1 >= 0 and nums1[p1] not in duplicates:
                sum1 += nums1[p1]
                p1 -= 1
            while p2 >= 0 and nums2[p2] not in duplicates:
                sum2 += nums2[p2]
                p2 -= 1
            if nums1[p1] == nums2[p2]:
                current_max += max(sum1, sum2) + nums1[p1]
            else:
                current_max += max(sum1, sum2)
            p1 -= 1
            p2 -= 1
        if p1 >= 0: current_max += sum(nums1[:p1 + 1])
        if p2 >= 0: current_max += sum(nums2[:p2 + 1])
        return current_max%(10**9 + 7)
# leetcode submit region end(Prohibit modification and deletion)
