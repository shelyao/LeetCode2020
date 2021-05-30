# Given a balanced parentheses string s, compute the score of the string based o
# n the following rule: 
# 
#  
#  () has score 1 
#  AB has score A + B, where A and B are balanced parentheses strings. 
#  (A) has score 2 * A, where A is a balanced parentheses string. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: s = "(())"
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: s = "()()"
# Output: 2
#  
# 
#  Example 4: 
# 
#  
# Input: s = "(()(()))"
# Output: 6
#  
# 
#  
# 
#  Note: 
# 
#  
#  s is a balanced parentheses string, containing only ( and ). 
#  2 <= s.length <= 50 
#  
#  Related Topics String Stack 
#  👍 2244 👎 70


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = level = 0
        for i, x in enumerate(s):
            if x == '(':
                level += 1
            else:
                level -= 1
                if i > 0 and s[i-1] == '(':
                    res += 1 << level
        return res
# leetcode submit region end(Prohibit modification and deletion)
