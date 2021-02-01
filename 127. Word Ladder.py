class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        stack = deque([beginWord])
        wordSet = set(wordList)
        visited = set([beginWord])
        res = 1
        while stack:
            n = len(stack)
            for i in range(n):
                word = stack.popleft()
                if word == endWord: return res
                for j, letter in enumerate(word):
                    for k in range(ord('a'), ord('z')+1):
                        if letter == chr(k): continue
                        next_word = word[:j] + chr(k) + word[j+1:]
                        if next_word in wordSet and next_word not in visited:
                            stack.append(next_word)
                            visited.add(next_word)
            res += 1
        return 0