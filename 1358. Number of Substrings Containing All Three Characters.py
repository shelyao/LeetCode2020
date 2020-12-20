class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if not s or len(s) < 3: return 0
        Counter = defaultdict(int)
        N, res = len(s), 0
        l = 0
        for r in range(N):
            Counter[s[r]] += 1
            while Counter['a'] > 0 and Counter['b'] > 0 and Counter['c'] > 0:
                Counter[s[l]] -= 1
                l += 1
            res += l
        return res