class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0: return 0
        left = res = 0
        substrMap = {}
        for right, char in enumerate(s):
            if char not in substrMap:
                substrMap[char] = right
            else:
                left = max(left, substrMap[char] + 1)
                substrMap[char] = right
            #print(left, right, substrMap)
            res = max(res, right - left + 1)
        return res