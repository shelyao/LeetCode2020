# Given a string s. An awesome substring is a non-empty substring of s such that
#  we can make any number of swaps in order to make it palindrome. 
# 
#  Return the length of the maximum length awesome substring of s. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "3242415"
# Output: 5
# Explanation: "24241" is the longest awesome substring, we can form the palindr
# ome "24142" with some swaps.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "12345678"
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: s = "213123"
# Output: 6
# Explanation: "213123" is the longest awesome substring, we can form the palind
# rome "231132" with some swaps.
#  
# 
#  Example 4: 
# 
#  
# Input: s = "00"
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  s consists only of digits. 
#  
#  Related Topics String Bit Manipulation 
#  👍 338 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        state_idx = {0: -1}
        res, n = 0, len(s)
        for i in range(n):
            mask ^= 1 << int(s[i])
            if mask not in state_idx: state_idx[mask] = i
            # print(s[i], mask, 1 << int(s[i]), state_idx)
            if mask in state_idx:
                res = max(res, i - state_idx[mask])
            state = 0
            for a in range(10):
                new_mask = mask ^ 1 << a
                if new_mask in state_idx:
                    state = new_mask
                    # print(a, new_mask)
                    res = max(res, i - state_idx[state])
        # print(res)
        return res



# leetcode submit region end(Prohibit modification and deletion)