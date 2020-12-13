class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        union, curr = [], ['']
        for char in expression:
            if char == ' ': continue
            if char.isalpha():
                curr = [c + char for c in curr]
            elif char == ',':
                union += curr
                curr = ['']
            elif char == '{':
                stack.append(union)
                stack.append(curr)
                union, curr = [], ['']
            else:
                pre, preU = stack.pop(), stack.pop()
                curr = [p + r for p in pre for r in curr + union]
                union = preU
        return sorted(set(union + curr))