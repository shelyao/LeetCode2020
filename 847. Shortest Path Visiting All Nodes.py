class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        heap = []
        visited = set()
        target = 2**n - 1
        for start in range(n):
            status = 1 << start
            heappush(heap, (0, start, status))
            visited.add((start, status))
        while heap:
            steps, current, status = heappop(heap)
            if status == target: 
                return steps
            for nb in graph[current]:
                new_s = status | 1 << nb
                if (nb, new_s) not in visited:
                    visited.add((nb, new_s))
                    heappush(heap, (steps + 1, nb, new_s))
        
        return -1
                    