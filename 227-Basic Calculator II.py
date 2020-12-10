class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        stack, sign = [], '+'
        num = 0
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char in ('+', '-', '*', '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(num*(-1))
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    preNum = stack.pop()
                    if preNum > 0: stack.append(preNum//num)
                    else: stack.append(-(abs(preNum)//num))
                num = 0
                sign = char
        return sum(stack)