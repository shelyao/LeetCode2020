# Given a string s of '(' , ')' and lowercase English characters. 
# 
#  Your task is to remove the minimum number of parentheses ( '(' or ')', in any
#  positions ) so that the resulting parentheses string is valid and return any va
# lid string. 
# 
#  Formally, a parentheses string is valid if and only if: 
# 
#  
#  It is the empty string, contains only lowercase characters, or 
#  It can be written as AB (A concatenated with B), where A and B are valid stri
# ngs, or 
#  It can be written as (A), where A is a valid string. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#  
# 
#  Example 4: 
# 
#  
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  s[i] is one of '(' , ')' and lowercase English letters. 
#  Related Topics String Stack 
#  👍 2158 👎 49


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = []
        temp = ''
        balance = 0
        for i, x in enumerate(s):
            temp += x
            if x not in '()': continue
            if x == '(': balance += 1
            if x == ')':
                balance -= 1
                if balance < 0:
                    temp = temp[:-1]
                    balance = 0
        balance = 0
        res = ''
        for i, x in enumerate(temp[::-1]):
            res += x
            if x not in '()': continue
            if x == ')': balance += 1
            if x == '(':
                balance -= 1
                if balance < 0:
                    res = res[:-1]
                    balance = 0
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
