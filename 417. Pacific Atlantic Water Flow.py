class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix) == 0: return []
        m, n = len(matrix), len(matrix[0])
        set1 = set()
        set2 = set()
        def dfs(x, y, res):
            m, n = len(matrix), len(matrix[0])
            res.add((x, y))
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] < matrix[x][y] or (nx, ny) in res:
                    continue
                dfs(nx, ny, res)
        for i in range(m):
            dfs(i, 0, set1)
        for i in range(1, n):
            dfs(0, i, set1)
        for i in range(m):
            dfs(i, n-1, set2)
        for i in range(0, n-1):
            dfs(m-1, i, set2)
        return [[x, y] for x,y in (set1&set2)]
        
        
            
        