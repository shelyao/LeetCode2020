# Given a string containing just the characters '(' and ')', find the length of 
# the longest valid (well-formed) parentheses substring. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#  
# 
#  Example 2: 
# 
#  
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#  
# 
#  Example 3: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 3 * 104 
#  s[i] is '(', or ')'. 
#  
#  Related Topics String Dynamic Programming 
#  👍 5240 👎 190


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        left = right = 0
        for x in s:
            if x == '(': left += 1
            if x == ')': right += 1
            if left == right:
                res = max(res, 2*left)
            if right > left:
                left = right = 0
        left = right = 0
        for x in s[::-1]:
            if x == ')': left += 1
            if x == '(': right += 1
            if left == right:
                res = max(res, left*2)
            if right > left:
                left = right = 0
        return res
# leetcode submit region end(Prohibit modification and deletion)
