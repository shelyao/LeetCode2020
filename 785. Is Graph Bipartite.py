class Solution:
    def isBipartite_bfs(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0 for i in range(n)]
        stack = deque([0])
        for node in range(n):
            if not visited[node]: visited[node] = 1
            stack = [node]
            while stack:
                nd = stack.pop()
                for neighbor in graph[nd]:
                    if visited[neighbor] != 0:
                        if visited[neighbor] == visited[nd]: return False
                    else:
                        visited[neighbor] = -visited[nd]
                        stack.append(neighbor)
        return True
        
    # dfs
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0 for i in range(n)]
        
        def dfs(visited, node, val):
            if visited[node] != 0: 
                return visited[node] == val
            visited[node] = val
            for neighbor in graph[node]:
                if not dfs(visited, neighbor, -val): return False
            return True
                
        for i in range(n):
            if visited[i] == 0:
                if not dfs(visited, i, 1): return False
        return True