class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        if n < k: return s
        stack = []
        for c in s:
            if not stack or c != stack[-1][0]: 
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        return ''.join([c[0]*c[1] for c in stack])