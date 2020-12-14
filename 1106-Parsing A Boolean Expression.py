class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack, value = [], []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char in '&|!':
                expr = char
            elif char in 'tf':
                value.append(char == 't')
            elif char == '(':
                stack.append(value)
                stack.append(expr)
                value = []
            elif char == ')':
                expr = stack.pop()
                _value = stack.pop()
                if expr == '&': _value.append(all(value))
                elif expr == '|': _value.append(any(value))
                else: _value.append(not all(value))
                value = _value
            i += 1
        return value[0]