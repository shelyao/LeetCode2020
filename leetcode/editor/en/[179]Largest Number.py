# Given a list of non-negative integers nums, arrange them such that they form t
# he largest number. 
# 
#  Note: The result may be very large, so you need to return a string instead of
#  an integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,2]
# Output: "210"
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1]
# Output: "1"
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [10]
# Output: "10"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 109 
#  
#  Related Topics Sort 
#  👍 3099 👎 323


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0: return ""
        if len(nums) == 1: return str(nums[0])
        heap = []
        res = ""
        for num in nums:
            ch = str(num)
            while len(ch) < 5:
                ch += ch
            n = len(ch)
            ch_n = int(ch + ch[:9-n])
            heappush(heap, (-ch_n, str(num)))
        while heap:
            to_add = heappop(heap)[1]
            res += to_add
        return res if res[0] != '0' else '0'
# leetcode submit region end(Prohibit modification and deletion)
