class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(start, subset, res):
            for i in range(start, len(S)):
                s = S[i]
                if s.isdigit():
                    subset += s
                else:
                    s = s.lower()
                    backtrack(i+1, subset + s, res)
                    backtrack(i+1, subset + s.upper(), res)
            if len(subset) == len(S):
                res.append(subset)
                return
        res = []
        backtrack(0, '', res)
        return res