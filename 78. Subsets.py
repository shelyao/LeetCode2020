class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subset, nums):
            if nums == []:
                return [subset]
            return backtrack(subset, nums[1:]) + backtrack(subset + [nums[0]], nums[1:])
        return backtrack([], nums)