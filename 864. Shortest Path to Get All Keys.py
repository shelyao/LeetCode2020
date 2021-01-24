class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        num_keys = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = i, j
                elif 'a' <= grid[i][j] <= 'f':
                    num_keys += 1
        heap = []
        state = 0
        heappush(heap, (0, start, state))
        visited = set([start, state])
        while heap:
            steps, current, state = heappop(heap)
            if state == (1 << num_keys) - 1: return steps
            x0, y0 = current
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                x1, y1 = x0 + dx, y0 + dy
                if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] != '#' and ((x1, y1), ):
                    if 'A' <= grid[x1][y1] <= 'F' and not (state & 1 << ord(grid[x1][y1]) - ord('A')):
                        continue
                    if 'a' <= grid[x1][y1] <= 'f':
                        new_s = state | 1 << ord(grid[x1][y1]) - ord('a')
                    else: new_s = state
                
                    if ((x1, y1), new_s) not in visited:
                        visited.add(((x1, y1), new_s))
                        heappush(heap, (steps + 1, (x1, y1), new_s))
        
        return -1
                        
                
        
        