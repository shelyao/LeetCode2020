class Solution:
        # optimize
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i%n]
            if i < n:
                stack.append(i)
        return res
    
    def nextGreaterElements0(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        stack = []
        num_map = {}
        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                if stack[-1] in num_map: stack.pop()
                else: num_map[stack.pop()] = nums[i%n]
            if i < n:
                stack.append(i)
        print(num_map)
        for idx, num in enumerate(nums):
            res.append(num_map.get(idx, -1))
        
        return res
        
    