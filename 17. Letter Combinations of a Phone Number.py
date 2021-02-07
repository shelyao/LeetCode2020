class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {2:'abc',
                 3:'def',
                 4:'ghi',
                 5:'jkl',
                 6:'mno',
                 7:'pqrs',
                 8:'tuv',
                 9:'wxyz'}
        def dfs(res, current, digits):
            if not digits:
                res.append(current)
                return
            for letter in digitMap[int(digits[0])]:
                dfs(res, current + letter, digits[1:])
        
        res = []
        if digits: dfs(res, '', digits)
        return res
                