class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(pos, subset, res):
            if pos == len(word):
                res.append(subset)
                return
            if subset and subset[-1].isdigit():
                cnt = int(subset[-1]) + 1
                dfs(pos+1, subset[:-1] + str(cnt), res)
            else:
                dfs(pos+1, subset + '1', res)
            dfs(pos+1, subset+word[pos], res)
        res = []
        dfs(0, "", res)
        return res