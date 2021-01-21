class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        stack = deque([(0, deepcopy(mat))])
        res = float('inf')
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                l = len(stack)
                for k in range(l):
                    flip, current = stack.popleft()
                    if sum(sum(current, [])) == 0: res = min(res, flip)
                    #add flip i, j
                    nex = deepcopy(current)
                    nex[i][j] = 1 - nex[i][j]
                    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                        new_x, new_y = i + dx, j + dy
                        if 0 <= new_x < m and 0 <= new_y < n:
                            nex[new_x][new_y] = 1 - nex[new_x][new_y]
                    stack.append((flip + 1, nex))
                    #not flip i, j
                    stack.append((flip, deepcopy(current)))
        while stack:
            flip, current = stack.pop()
            if sum(sum(current, [])) == 0: res = min(res, flip)
        
        return res if res != float('inf') else -1
                    
                