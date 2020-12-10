class Solution:
    def __init__(self):
        self.i = 0
    def calculate(self, s: str) -> int:
        stack, num = [], 0
        operator = '+'
        ans = 0
        while self.i < len(s):
            char = s[self.i]
            self.i += 1
            if char.isdigit():
                num = num*10 + int(char)
            if char == '(': num = self.calculate(s)
            if self.i == len(s) or char in '+-*/)':
                if operator == '+': stack.append(num)
                elif operator == '-': stack.append(-num)
                elif operator == '*': stack.append(stack.pop()*num)
                elif operator == '/': 
                    preNum = stack.pop()
                    if preNum > 0: stack.append(preNum//num)
                    else: stack.append(-(abs(preNum)//num))
                operator = char
                num = 0
            if char == ')': break
        return sum(stack)