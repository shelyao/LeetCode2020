# Given a string s containing only three types of characters: '(', ')' and '*', 
# return true if s is valid. 
# 
#  The following rules define a valid string: 
# 
#  
#  Any left parenthesis '(' must have a corresponding right parenthesis ')'. 
#  Any right parenthesis ')' must have a corresponding left parenthesis '('. 
#  Left parenthesis '(' must go before the corresponding right parenthesis ')'. 
# 
#  '*' could be treated as a single right parenthesis ')' or a single left paren
# thesis '(' or an empty string "". 
#  
# 
#  
#  Example 1: 
#  Input: s = "()"
# Output: true
#  Example 2: 
#  Input: s = "(*)"
# Output: true
#  Example 3: 
#  Input: s = "(*))"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 100 
#  s[i] is '(', ')' or '*'. 
#  
#  Related Topics String 
#  👍 2406 👎 68


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for x in s:
            if x == '(': lo += 1
            else: lo -= 1
            if x != ')': hi += 1
            else: hi -= 1
            if hi < 0: break
            lo = max(lo, 0)
        return lo == 0

# leetcode submit region end(Prohibit modification and deletion)
