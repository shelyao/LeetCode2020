class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        visited = set()
        def backtrack(nums, res, subset, visited):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            for i in range(len(nums)):
                if nums[i] in visited: continue
                visited.add(nums[i])
                subset.append(nums[i])
                backtrack(nums, res, subset, visited)
                visited.remove(nums[i])
                subset.pop()
        backtrack(nums, res, subset, visited)
        return res
            