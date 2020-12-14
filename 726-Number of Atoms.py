class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, N = 0, len(formula)
        stack = [defaultdict(int)]
        while i < N:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                curr = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                Num = int(formula[i_start:i] or 1)
                for name, count in curr.items():
                    stack[-1][name] += count*Num
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start:i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                Num = int(formula[i_start:i] or 1)
                stack[-1][name] += Num
        
        return ''.join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                      for name in sorted(stack[-1]))