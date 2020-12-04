class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        if n <= k: return "0"
        for s in num:
            while stack and stack[-1] > s and k > 0:
                stack.pop()
                k -= 1
            if stack and stack[0] == "0": stack.pop(0)
            stack.append(s)
        
        if k > 0: stack = stack[:-k]
        return ''.join(stack) if stack else "0"