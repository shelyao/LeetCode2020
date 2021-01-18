class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        boundry = []
        visited = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            heappush(boundry, (heightMap[i][0], i, 0))
            heappush(boundry, (heightMap[i][n-1], i, n-1))
            visited[i][0] = 1
            visited[i][n-1] = 1
        for i in range(1, n-1):
            heappush(boundry, (heightMap[0][i], 0, i))
            heappush(boundry, (heightMap[m-1][i], m-1, i))
            visited[0][i] = 1
            visited[m-1][i] = 1
            
        while boundry:
            local_min, x, y = heappop(boundry)
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == 0:
                    heappush(boundry, (max(local_min, heightMap[new_x][new_y]), new_x, new_y))
                    visited[new_x][new_y] = 1
                    res += max(0, local_min - heightMap[new_x][new_y])
        return res