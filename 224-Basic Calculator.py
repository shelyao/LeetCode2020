class Solution:
    def calculate(self, s: str) -> int:
        stack, res =[], 0
        pos, sign = 0, 1
        num, n = 0, len(s)
        while pos < n:
            if s[pos] == " ": 
                pos += 1
                continue
            while pos < n and s[pos].isdigit():
                num = 10*num + int(s[pos])
                pos += 1
            if pos == n: break
            if s[pos] == "-":
                res += sign*num
                sign = -1
                num = 0
            elif s[pos] == "+":
                res += sign*num
                sign = 1
                num = 0
            elif s[pos] == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif s[pos] == ")":
                res += num*sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
            pos += 1
            
        return res + sign*num
            
            
            