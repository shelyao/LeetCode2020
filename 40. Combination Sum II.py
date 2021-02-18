class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, visited, total, subset, res):
            if total == target:
                res.append(subset[:])
                return
            for i in range(start, len(candidates)):
                if total > target: break 
                if not (i > start and candidates[i] == candidates[i-1] and visited[i-1] == 0):
                    visited[i] = 1
                    subset.append(candidates[i])
                    backtrack(i+1, visited, total + candidates[i], subset, res)
                    visited[i] = 0
                    subset.pop()
        res = []
        visited = [0]*len(candidates)
        candidates.sort()
        backtrack(0, visited, 0, [], res)
        return res