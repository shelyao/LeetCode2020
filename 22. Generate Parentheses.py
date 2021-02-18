class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(leftnum, rightnum, subset, res):
            if leftnum == n and leftnum == rightnum:
                res.append(subset)
                return
            if leftnum < n and rightnum <= leftnum:
                subset += '('
                backtrack(leftnum + 1, rightnum, subset, res)
                subset = subset[:-1]
            if leftnum <= n and rightnum < leftnum:
                subset += ')'
                backtrack(leftnum, rightnum + 1, subset, res)
                subset = subset[:-1]
        res = []
        backtrack(0, 0, '', res)
        return res