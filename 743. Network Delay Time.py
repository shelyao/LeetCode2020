class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distance = {node:float('inf') for node in range(1, N+1)}
        def dfs(node, time):
            if time >= distance[node]: return
            distance[node] = time
            for neighbor, dist in graph[node]:
                dfs(neighbor, time + dist)
        
        dfs(K, 0)
        res = max(distance.values())
        return -1 if res == float('inf') else res
                    
            
        
        
        
            