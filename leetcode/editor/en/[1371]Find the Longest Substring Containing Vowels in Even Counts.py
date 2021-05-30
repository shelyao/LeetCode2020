# Given the string s, return the size of the longest substring containing each v
# owel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear a
# n even number of times. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each 
# of the vowels: e, i and o and zero of the vowels: a and u.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because al
# l vowels: a, e, i, o and u appear zero times.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 x 10^5 
#  s contains only lowercase English letters. 
#  
#  Related Topics String 
#  👍 629 👎 26


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        owel_dict = {0:-1}
        res = state = 0
        owels = 'aeiou'
        for i, x in enumerate(s):
            idx = owels.find(x)
            if idx >= 0:
                state ^= 1 << idx
            if state not in owel_dict: owel_dict[state] = i
            res = max(res, i - owel_dict[state])
        return res
# leetcode submit region end(Prohibit modification and deletion)
