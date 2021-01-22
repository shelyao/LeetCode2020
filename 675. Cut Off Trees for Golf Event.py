class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        to_cut = []
        res = 0
        m, n = len(forest), len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1: to_cut.append((forest[i][j], i, j))
        to_cut.sort(reverse = True)
        def bfs(start, x, y):
            if start[0] == x and start[1] == y: return 0
            m, n = len(forest), len(forest[0])
            visited = [[0]*n for _ in range(m)]
            stack = deque([start])
            res = 0
            while stack:
                k = len(stack)
                for i in range(k):
                    x0, y0 = stack.popleft()
                    if x0 == x and y0 == y: return res
                    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                        new_x, new_y = x0 + dx, y0 + dy
                        if 0 <= new_x < m and 0 <= new_y < n and forest[new_x][new_y] > 0 and visited[new_x][new_y] == 0:
                            visited[new_x][new_y] = 1
                            stack.append((new_x, new_y))
                res += 1
            return -1
        
        init = (0, 0)
        while to_cut:
            num, x, y = to_cut.pop()
            steps = bfs(init, x, y)
            if steps == -1: return -1
            res += steps
            init = (x, y)
        
        return res
            