class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        heap = []
        heappush(heap, (0, "", ball[0], ball[1]))
        visited = defaultdict(int)
        visited[tuple(ball)] = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rolling = ["r", "l", "d", "u"]
        routes = []
        while heap:
            dist, path, x, y = heappop(heap)
            if x == hole[0] and y == hole[1]:
                routes.append(path)
                continue
            for i in range(4):
                dx, dy = directions[i][0], directions[i][1]
                new_x, new_y = x, y
                step = 0
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    step += 1
                    new_x += dx
                    new_y += dy
                    if new_x == hole[0] and new_y == hole[1]:
                        #routes.append((dist + step, path + rolling[i]))
                        break
                if new_x != x or new_y != y:
                    if (new_x, new_y) not in visited or dist + step <= visited[(new_x, new_y)]:
                        visited[(new_x, new_y)] = dist + step
                        heappush(heap, (dist + step, path + rolling[i], new_x, new_y))
        #print(routes)
        return "impossible" if routes == [] else routes[0]
                        