class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def helper(left, right):
            if right - left < k: return 0
            counter = Counter(s[left:right])
            for i in range(left, right):
                if counter[s[i]] >= k: continue
                next_char = i + 1
                while (next_char < right and counter[s[next_char]] < k):
                    next_char += 1
                return max(helper(left, i), helper(next_char, right))
            return right - left
        
        return helper(0, len(s))