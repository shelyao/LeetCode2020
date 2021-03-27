# You are given an array of integers nums (0-indexed) and an integer k. 
# 
#  The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., num
# s[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j. 
# 
#  Return the maximum possible score of a good subarray. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (
# 5-1+1) = 3 * 5 = 15. 
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (
# 4-0+1) = 4 * 5 = 20.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 2 * 104 
#  0 <= k < nums.length 
#  
#  Related Topics Greedy 
#  👍 212 👎 14


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right = k
        n = len(nums)
        res = nums[k]
        heap = [nums[k]]
        while left > 0 or right < n - 1:
            if left > 0 and right < n - 1:
                if nums[left-1] > nums[right+1]:
                    heappush(heap, nums[left-1])
                    left -= 1
                else:
                    heappush(heap, nums[right+1])
                    right += 1
            elif left > 0:
                heappush(heap, nums[left - 1])
                left -= 1
            else:
                heappush(heap, nums[right + 1])
                right += 1
            res = max(res, heap[0]*(right-left+1))
        return res


# leetcode submit region end(Prohibit modification and deletion)
