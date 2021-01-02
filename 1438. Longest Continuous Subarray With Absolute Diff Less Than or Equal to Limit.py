class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = left = 0
        n = len(nums)
        minStack = deque()
        maxStack = deque()
        for right, num in enumerate(nums):
            while minStack and nums[minStack[-1]] > nums[right]:
                minStack.pop()
            minStack.append(right)
            #print(minStack)
            while maxStack and nums[maxStack[-1]] < nums[right]:
                maxStack.pop()
            maxStack.append(right)
            #print(maxStack)
            while minStack and num - nums[minStack[0]] > limit:
                left = minStack.popleft() + 1
            while maxStack and nums[maxStack[0]] - num > limit:
                left = max(left, maxStack.popleft() + 1)
            res = max(res, right - left + 1)
        return res
            