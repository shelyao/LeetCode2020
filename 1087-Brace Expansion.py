class Solution:
    # Stack
    def expand(self, S: str) -> List[str]:
        res = [[]]
        in_bracket, bracket = False, []
        for char in S:
            #print(res)
            if char in ',': continue
            if char == '{':
                in_bracket = True
                bracket = []
            elif char == '}':
                in_bracket = False
                res = [w1 + [w2] for w1 in res for w2 in sorted(bracket)]
                bracket = []
            elif in_bracket:
                bracket.append(char)
            else:
                res = [w1 + [char] for w1 in res]
        return [''.join(w) for w in res]
    
    #dfs
    def expand(self, S: str) -> List[str]:
        res = []
        def dfs(s, i, word, res):
            if i == len(s):
                res.append(word)
                return
            if s[i] != '{':
                dfs(s, i+1, word + s[i], res)
            else:
                i += 1
                bracket = []
                while s[i] != '}':
                    if s[i] != ',':
                        bracket.append(s[i])
                    i += 1
                for c in bracket:
                    dfs(s, i+1, word + c, res)
        dfs(S, 0, '', res)
        return sorted(res)
            