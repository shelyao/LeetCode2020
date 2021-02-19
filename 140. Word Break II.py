class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = defaultdict(list)
        def helper(s):
            if not s: return [[]]
            if s in memo:
                return memo[s]
            for endIdx in range(1, len(s)+1):
                word = s[:endIdx]
                if word in wordDict:
                    for sub in helper(s[endIdx:]):
                        memo[s].append([word] + sub)
            return memo[s]
        helper(s)
        return [' '.join(words) for words in memo[s]]