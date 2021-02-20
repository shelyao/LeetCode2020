class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(subset, start, res):
            if start == len(s):
                res.append(subset[:])
                return
            for i in range(start, len(s)):
                substr = s[start : i+1]
                if substr == substr[::-1]:
                    subset.append(substr)
                    backtrack(subset, i + 1, res)
                    subset.pop()
        res = []
        backtrack([], 0, res)
        return res