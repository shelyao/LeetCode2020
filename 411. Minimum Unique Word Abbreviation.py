class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        def dfs(pos, subset, res):
            if pos == len(target):
                res.append(subset)
                return
            if subset and subset[-1].isdigit():
                if len(subset) >= 2 and subset[-2].isdigit():
                    cnt = int(subset[-2:]) + 1
                    dfs(pos+1, subset[:-2] + str(cnt), res)
                else:
                    cnt = int(subset[-1]) + 1
                    dfs(pos+1, subset[:-1] + str(cnt), res)
            else:
                dfs(pos+1, subset + '1', res)
            dfs(pos+1, subset+target[pos], res)
        words = []
        queue = []
        dfs(0, "", words)
        for word in words:
            heappush(queue, (len(word), word))
        
        while queue:
            find = True
            _, abbr = heappop(queue)
            for word in dictionary:
                #print(abbr)
                if self.validWordAbbreviation(word, abbr):
                    find = False
                    continue
            if find: return abbr
            
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx, n = 0, len(word)
        k = len(abbr)
        if k > n: return False
        start = 0
        while start < k:
            num = ''
            while start < k and abbr[start].isdigit():
                num += abbr[start]
                start += 1
            if num != '':
                if num[0] == '0': return False
                idx += int(num)
            else:
                if idx >= n or abbr[start] != word[idx]:
                    return False
                else:
                    idx += 1
                start += 1
        return idx == n
    