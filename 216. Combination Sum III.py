class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, total, cnt, subset, res):
            if cnt == k and total == n:
                res.append(subset[:])
                return
            for i in range(start, 10):
                if i + total <= n and cnt + 1 <= k:
                    subset.append(i)
                    backtrack(i + 1, i + total, cnt + 1, subset, res)
                    subset.pop()
        res = []
        backtrack(1, 0, 0, [], res)
        return res