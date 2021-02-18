class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, subset, k, res):
            if k == 0:
                res.append(subset[:])
                return
            for i in range(start, n+1):
                subset.append(i)
                backtrack(i+1, subset, k-1, res)
                subset.pop()
        res = []
        backtrack(1, [], k, res)
        return res