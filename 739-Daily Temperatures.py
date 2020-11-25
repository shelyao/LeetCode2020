class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        for i, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res