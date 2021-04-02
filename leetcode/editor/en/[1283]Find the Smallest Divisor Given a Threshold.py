# Given an array of integers nums and an integer threshold, we will choose a pos
# itive integer divisor, divide all the array by it, and sum the division's result
# . Find the smallest divisor such that the result mentioned above is less than or
#  equal to threshold. 
# 
#  Each result of the division is rounded to the nearest integer greater than or
#  equal to that element. (For example: 7/3 = 3 and 10/2 = 5). 
# 
#  It is guaranteed that there will be an answer. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 th
# e sum will be 5 (1+1+1+2). 
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [21212,10101,12121], threshold = 1000000
# Output: 1
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [2,3,5,7,11], threshold = 11
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 104 
#  1 <= nums[i] <= 106 
#  nums.length <= threshold <= 106 
#  
#  Related Topics Binary Search 
#  👍 713 👎 128


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        n = len(nums)
        if n > threshold: return -1
        if n == threshold: return r
        res = r
        while l <= r:
            mid = l + (r-l)//2
            div = 0
            for i in range(n):
                div += math.ceil(nums[i]/mid)
                if div > threshold: break
            if div <= threshold:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
