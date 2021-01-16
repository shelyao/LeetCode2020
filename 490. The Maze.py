class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        stack = deque([(start[0], start[1], -1, -1)])
        directions  = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set([(start[0], start[1])])
        
        def hasNext(x, y, d, directions):
            dx, dy = directions[d]
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != 1:
                return True
            return False
            
        while stack:
            #print(stack)
            x, y, pd, d = stack.pop()
            if x == destination[0] and y == destination[1] and not hasNext(x, y, pd, directions):
                return True
            if d == -1:
                for i in range(4):
                    new_x, new_y = x + directions[i][0], y + directions[i][1]
                    if hasNext(new_x, new_y, i, directions): next_d = i
                    else: 
                        next_d = -1
                    if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y, next_d) not in visited and maze[new_x][new_y] != 1:
                        stack.append((new_x, new_y, i, next_d))
                        visited.add((new_x, new_y, next_d))
            else:
                new_x, new_y = x + directions[d][0], y + directions[d][1]
                if hasNext(new_x, new_y, d, directions): next_d = d
                else: 
                    next_d = -1
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y, next_d) not in visited and maze[new_x][new_y] != 1:
                        stack.append((new_x, new_y, d, next_d))
                        visited.add((new_x, new_y, next_d))
        
        return False
                
            