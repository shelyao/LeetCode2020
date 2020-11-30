class Solution:
    # keep track of the smallest third number when looping through nums list
    def find132pattern(self, nums: List[int]) -> bool:
        n, stack = len(nums), []
        third = float('-inf')
        for i in range(n-1, -1, -1):
            if nums[i] < third:
                return True
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            stack.append(nums[i])
        return False
    
    # n^2: TLE
    def find132pattern0(self, nums: List[int]) -> bool:
        n, stack = len(nums), []
        for i in range(n - 2):
            stack = [nums[i]]
            for j in range(i + 1, n):
                if stack and nums[j] > stack[-1]:
                    while len(stack) > 1:
                        stack.pop()
                    stack.append(nums[j])
                elif len(stack) > 1 and nums[i] < nums[j] and stack[-1] > nums[j]:
                    return True
        return False
                    
            