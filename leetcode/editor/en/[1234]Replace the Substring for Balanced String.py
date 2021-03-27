# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and
#  'R'. 
# 
#  A string is said to be balanced if each of its characters appears n/4 times w
# here n is the length of the string. 
# 
#  Return the minimum length of the substring that can be replaced with any othe
# r string of the same length to make the original string s balanced. 
# 
#  Return 0 if the string is already balanced. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced. 
# 
#  Example 2: 
# 
#  
# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is ba
# lanced.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER". 
#  
# 
#  Example 4: 
# 
#  
# Input: s = "QQQQ"
# Output: 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  s.length is a multiple of 4 
#  s contains only 'Q', 'W', 'E' and 'R'.
#  
#  Related Topics Two Pointers String 
#  👍 474 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s) // 4
        n = len(s)
        res = n
        counter = Counter(s)
        to_move = set()
        for char in "WERQ":
            if counter[char] > target:
                to_move.add(char)
        if len(to_move) == 0: return 0
        left = 0
        for right in range(n):
            counter[s[right]] -= 1
            if counter[s[right]] == target:
                to_move.remove(s[right])
            while left <= right and len(to_move) == 0:
                char = s[left]
                res = min(res, right - left + 1)
                counter[char] += 1
                if counter[char] > target:
                    to_move.add(char)
                # print(left, right, to_move)
                left += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
