class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, indegree = defaultdict(list), defaultdict(int)
        for word in words: 
            for char in word:
                indegree[char]
        for i, word in enumerate(words[:-1]):
            for j, char in enumerate(word):
                if j >= len(words[i+1]): return ""
                if char != words[i+1][j]:
                    graph[char].append(words[i+1][j])
                    indegree[words[i+1][j]] += 1
                    break
        deq = deque([c for c in indegree if indegree[c] == 0])
        print(graph, indegree)
        res = []
        while deq:
            curr = deq.popleft()
            res.append(curr)
            for char in graph[curr]:
                indegree[char] -= 1
                if indegree[char] == 0:
                    deq.append(char)
        if len(res) != len(indegree): return ""
        return ''.join(res)