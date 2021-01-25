class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [0, [0, 1], [0, -1], [1, 0], [-1, 0]]
        graph = defaultdict(list)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                for k in range(1, 5):
                    dx, dy = directions[k]
                    if i + dx < 0 or i + dx >= m or j + dy < 0 or j + dy >= n: continue
                    if k == grid[i][j]: graph[(i, j)].append((k, 0))
                    else: graph[(i, j)].append((k, 1))
        
        heap = []
        heappush(heap, (0, 0, 0))
        visited = defaultdict(int)
        visited[(0, 0)] = 0
        while heap:
            costs, x0, y0 = heappop(heap)
            if x0 == m - 1 and y0 == n - 1: return costs
            for k, cst in graph[(x0, y0)]:
                x1, y1 = x0 + directions[k][0], y0 + directions[k][1]
                cst1 = costs + cst
                if (x1, y1) not in visited or cst1 < visited[(x1, y1)]:
                    heappush(heap, (cst1, x1, y1))
                    visited[(x1, y1)] = cst1
        
        return -1