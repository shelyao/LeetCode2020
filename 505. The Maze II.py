class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        heap = []
        heappush(heap, (0, start[0], start[1]))
        visited = defaultdict(int)
        visited[tuple(start)] = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while heap:
            dist, x, y = heappop(heap)
            if x == destination[0] and y == destination[1]: return dist
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                step = 0
                while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] != 1:
                    new_x += dx
                    new_y += dy
                    step += 1
                new_x -= dx
                new_y -= dy
                if (new_x, new_y) not in visited or dist + step < visited[(new_x, new_y)]:
                    visited[(new_x, new_y)] = dist + step
                    heappush(heap, (dist + step, new_x, new_y))
        return -1