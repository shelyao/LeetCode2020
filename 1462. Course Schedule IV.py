class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        res = []
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
    
        def bfs(query, graph):
            visited = set()
            stack = deque([query[1]])
            while stack:
                curr = stack.popleft()
                if curr in visited: continue
                visited.add(curr)
                for p in graph[curr]:
                    if p == query[0]: return True
                    stack.append(p)
            return False
        
        for query in queries:
            if query[1] not in graph: res.append(False)
            else: res.append(bfs(query, graph))
        return res