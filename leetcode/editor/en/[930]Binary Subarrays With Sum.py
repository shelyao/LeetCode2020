# In an array nums of 0s and 1s, how many non-empty subarrays have sum goal? 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#  
# 
#  
# 
#  Note: 
# 
#  
#  nums.length <= 30000 
#  0 <= goal <= nums.length 
#  nums[i] is either 0 or 1. 
#  
#  Related Topics Hash Table Two Pointers 
#  👍 832 👎 35


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = [0]
        res = 0
        count = defaultdict(int)
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        for pre in prefixSum:
            res += count[pre]
            count[pre + goal] += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
