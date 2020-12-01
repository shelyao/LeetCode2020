class Solution:
    # optimize
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        m, n = len(pushed), len(popped)
        if m != n: return False
        k = 0
        for i in range(n):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[k]:
                stack.pop()
                k += 1
        return k == n
    
    def validateStackSequences0(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        m, n = len(pushed), len(popped)
        if m != n: return False
        k = 0
        for i in range(n):
            while stack and stack[-1] == popped[k]:
                stack.pop()
                k += 1
            if pushed[i] == popped[k]:
                k += 1
            elif pushed[i] != popped[k]:
                stack.append(pushed[i])
        for i in range(len(stack)):
            if popped[k] != stack.pop():
                return False
            k += 1
        return True
    
    
        