class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <= 1: return [nums]
        def backtrack(nums, res, subset, visited):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            for i in range(len(nums)):
                if visited[i] == 1: continue
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] == 0:
                    continue
                visited[i] = 1
                subset.append(nums[i])
                backtrack(nums, res, subset, visited)
                visited[i] = 0
                subset.pop()
        nums.sort()
        res, subset = [], []
        visited = [0]*len(nums)
        backtrack(nums, res, subset, visited)
        return res