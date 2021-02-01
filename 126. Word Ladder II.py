class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        visited = set([beginWord])
        stack = deque([(beginWord, [beginWord])])
        wordSet = set(wordList)
        if endWord not in wordSet: return []
        res = []
        complete = 0
        while stack:
            n = len(stack)
            for i in range(n):
                currWord, path = stack.popleft()
                for j, letter in enumerate(currWord):
                    for k in range(ord('a'), ord('z')+1):
                        if chr(k) == letter: continue
                        nextWord = currWord[:j] + chr(k) + currWord[j+1:]
                        if nextWord in wordSet:
                            visited.add(nextWord)
                            new_path = path + [nextWord]
                            stack.append((nextWord, new_path))
                            if nextWord == endWord:
                                res.append(new_path)
                                complete = 1
            if complete == 1: break
            wordSet -= visited
        return res