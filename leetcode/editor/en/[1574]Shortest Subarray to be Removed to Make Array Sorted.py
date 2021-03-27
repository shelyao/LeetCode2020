# Given an integer array arr, remove a subarray (can be empty) from arr such tha
# t the remaining elements in arr are non-decreasing. 
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  Return the length of the shortest subarray to remove. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The 
# remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4]. 
# 
#  Example 2: 
# 
#  
# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single
#  element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] o
# r [4,3,2,1].
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any
#  elements.
#  
# 
#  Example 4: 
# 
#  
# Input: arr = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10^5 
#  0 <= arr[i] <= 10^9 
#  
#  Related Topics Array Binary Search 
#  👍 515 👎 17


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if not arr or len(arr) <= 1: return 0
        n = len(arr)
        subleft = 0
        subright = n - 1
        while subleft < n - 1:
            if arr[subleft + 1] < arr[subleft]:
                break
            subleft += 1
        if subleft == n - 1: return 0
        while subright > 0:
            if arr[subright - 1] > arr[subright]:
                break
            subright -= 1
        if subright == n - 1: return n - subleft - 1 - (arr[subright] >= arr[subleft])

        def bisect(val, left, right):
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return right

        res = min(subright, n - subleft - 1)
        for i in range(subleft + 1):
            left_val = arr[i]
            right_start = bisect(left_val, subright, n - 1)
            res = min(res, right_start - i - 1 + (arr[right_start] < arr[i]))
        return res
# leetcode submit region end(Prohibit modification and deletion)
