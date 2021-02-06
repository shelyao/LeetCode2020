class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def backtrack(res, subset, start):
            res.append(subset[:])
            #print(res)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(res, subset, i + 1)
                subset.pop()
        backtrack(res, subset, 0)
        return res
    