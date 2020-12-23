class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n <= 2: return n
        left = res = 0
        letterDict = {}
        for right in range(n):
            letterDict[s[right]] = right
            while len(letterDict) > 2:
                if left == letterDict[s[left]]: 
                    del letterDict[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res
    