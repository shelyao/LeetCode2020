class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        res = grid[0][0]
        visited[0][0] = 1
        heap = []
        heappush(heap, (res, 0, 0))
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while heap:
            val, x, y = heappop(heap)
            res = max(res, val)
            if x == m-1 and y == n-1: return res
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or visited[new_x][new_y] == 1:
                    continue
                heappush(heap, (grid[new_x][new_y], new_x, new_y))
                visited[new_x][new_y] = 1
        return -1
                         
            