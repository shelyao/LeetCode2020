# Given a string s that contains parentheses and letters, remove the minimum num
# ber of invalid parentheses to make the input string valid. 
# 
#  Return all the possible results. You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()())()"
# Output: ["(())()","()()()"]
#  
# 
#  Example 2: 
# 
#  
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
#  
# 
#  Example 3: 
# 
#  
# Input: s = ")("
# Output: [""]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 25 
#  s consists of lowercase English letters and parentheses '(' and ')'. 
#  There will be at most 20 parentheses in s. 
#  
#  Related Topics Depth-first Search Breadth-first Search 
#  👍 3421 👎 159


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for x in s:
            left += x == '('
            if left == 0:
                right += x == ')'
            else:
                left -= x == ')'

        def is_valid(s):
            left = 0
            for x in s:
                left += (x == '(') - (x == ')')
                if left < 0: return False
            return left == 0

        def dfs(s, start, left, right, res):
            if left == 0 and right == 0:
                if is_valid(s):
                    res.append(s)
                return
            for i in range(start, len(s)):
                if i != start and s[i] == s[i-1]:
                    continue
                if s[i] in '()':
                    curr = s[:i] + s[i+1:]
                if left > 0 and s[i] == '(':
                    dfs(curr, i, left-1, right, res)
                if right > 0 and s[i] == ')':
                    dfs(curr, i, left, right-1, res)
        res = []
        dfs(s, 0, left, right, res)
        return res


# leetcode submit region end(Prohibit modification and deletion)
