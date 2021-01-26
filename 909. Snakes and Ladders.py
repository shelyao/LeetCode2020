class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        m = n*n
        visited = [0]*(n*n+1)
        visited[1] = 0
        heap = []
        heappush(heap, (0, 1))
        def get_position(current, n):
            if ceil(current/n)%2 != 0:
                r = n - ceil(current/n)
                c = current - (n - r - 1)*n - 1
            else:
                r = n - ceil(current/n)
                c = n - 1 - (current - (n - r - 1)*n - 1)
            return r, c
        #print(get_position(36, 6))
        while heap:
            steps, current = heappop(heap)
            if current == m: return steps
            for i in range(1, 7):
                nxt = current + i
                if nxt > m: continue
                nr, nc = get_position(nxt, n)
                if board[nr][nc] != -1:
                    nxt = board[nr][nc]
                    nr, nc = get_position(nxt, n)
                if visited[nxt] == 0:
                    visited[nxt] = steps + 1
                    heappush(heap, (steps + 1, nxt))
        #print(visited)
        return -1
                        