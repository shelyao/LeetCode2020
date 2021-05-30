# Given a parentheses string s containing only the characters '(' and ')'. A par
# entheses string is balanced if: 
# 
#  
#  Any left parenthesis '(' must have a corresponding two consecutive right pare
# nthesis '))'. 
#  Left parenthesis '(' must go before the corresponding two consecutive right p
# arenthesis '))'. 
#  
# 
#  In other words, we treat '(' as openning parenthesis and '))' as closing pare
# nthesis. 
# 
#  For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" a
# nd "(()))" are not balanced. 
# 
#  You can insert the characters '(' and ')' at any position of the string to ba
# lance it if needed. 
# 
#  Return the minimum number of insertions needed to make s balanced. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only 
# ')' matching. We need to to add one more ')' at the end of the string to be "(()
# )))" which is balanced.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
#  
# 
#  Example 4: 
# 
#  
# Input: s = "(((((("
# Output: 12
# Explanation: Add 12 ')' to balance the string.
#  
# 
#  Example 5: 
# 
#  
# Input: s = ")))))))"
# Output: 5
# Explanation: Add 4 '(' at the beginning of the string and one ')' at the end. 
# The string becomes "(((())))))))".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  s consists of '(' and ')' only. 
#  
#  Related Topics String Stack 
#  👍 325 👎 75


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0
        num_right = 0
        for x in s:
            if x == ')': num_right += 1
            elif x == '(':
                if num_right == 1:
                    res += 1
                    num_right = 0
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        res += 1
                stack.append('(')
            if num_right == 2:
                num_right = 0
                if len(stack) > 0:
                    stack.pop()
                else:
                    res += 1
        if num_right == 1:
            res += 1
            if len(stack) > 0:
                stack.pop()
            else:
                res += 1
        return res + len(stack)*2


# leetcode submit region end(Prohibit modification and deletion)
