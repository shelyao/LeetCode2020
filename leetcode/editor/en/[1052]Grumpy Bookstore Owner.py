# Today, the bookstore owner has a store open for customers.length minutes. Ever
# y minute, some number of customers (customers[i]) enter the store, and all those
#  customers leave after the end of that minute. 
# 
#  On some minutes, the bookstore owner is grumpy. If the bookstore owner is gru
# mpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0. When the booksto
# re owner is grumpy, the customers of that minute are not satisfied, otherwise th
# ey are satisfied. 
# 
#  The bookstore owner knows a secret technique to keep themselves not grumpy fo
# r X minutes straight, but can only use it once. 
# 
#  Return the maximum number of customers that can be satisfied throughout the d
# ay. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 mi
# nutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 
# = 16.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= X <= customers.length == grumpy.length <= 20000 
#  0 <= customers[i] <= 1000 
#  0 <= grumpy[i] <= 1 
#  Related Topics Array Sliding Window 
#  👍 700 👎 69


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if not customers or len(customers) == 0: return 0
        n = len(customers)
        n_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                n_satisfied += customers[i]
        if X == 0: return n_satisfied
        for i in range(X):
            if grumpy[i] == 1:
                n_satisfied += customers[i]

        left = 1
        res = n_satisfied
        while left < n - X + 1:
            if grumpy[left - 1] == 1:
                n_satisfied -= customers[left - 1]
            if grumpy[left + X - 1] == 1:
                n_satisfied += customers[left + X - 1]
            res = max(res, n_satisfied)
            left += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
