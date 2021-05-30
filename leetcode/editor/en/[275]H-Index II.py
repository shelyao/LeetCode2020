# Given an array of integers citations where citations[i] is the number of citat
# ions a researcher received for their ith paper and citations is sorted in an asc
# ending order, return compute the researcher's h-index. 
# 
#  According to the definition of h-index on Wikipedia: A scientist has an index
#  h if h of their n papers have at least h citations each, and the other n − h pa
# pers have no more than h citations each. 
# 
#  If there are several possible values for h, the maximum one is taken as the h
# -index. 
# 
#  You must write an algorithm that runs in logarithmic time. 
# 
#  
#  Example 1: 
# 
#  
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each o
# f them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remai
# ning two with no more than 3 citations each, their h-index is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: citations = [1,2,100]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  n == citations.length 
#  1 <= n <= 105 
#  0 <= citations[i] <= 1000 
#  citations is sorted in ascending order. 
#  
#  Related Topics Binary Search 
#  👍 551 👎 854


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        res = 0
        for i, c in enumerate(citations):
            curr = min(i+1, c)
            if curr > res:
                res = curr
            else: break
        return res
# leetcode submit region end(Prohibit modification and deletion)
