class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(Sum, start, subset, res):
            if Sum == target:
                res.append(subset[:])
                return
            for i in range(start, len(candidates)):
                if Sum <= target:
                    subset.append(candidates[i])
                    backtrack(Sum + candidates[i], i, subset, res)
                    subset.pop()
        
        backtrack(0, 0, [], res)
        return res
        
        