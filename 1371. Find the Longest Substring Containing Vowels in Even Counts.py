class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state_idx = {0:-1}
        res = state = 0
        vowels = 'aeiou'
        for i in range(len(s)):
            k = vowels.find(s[i])
            if k >= 0: state ^= 1 << k
            if state not in state_idx: state_idx[state] = i
            # right - left + 1
            res = max(res, i - (state_idx[state] + 1) + 1)
        return res