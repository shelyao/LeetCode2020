class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k: return n
        string_idx = {}
        left = res = 0
        for right, char in enumerate(s):
            string_idx[char] = right
            while len(string_idx) > k:
                if left == string_idx[s[left]]:
                    del string_idx[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res
        