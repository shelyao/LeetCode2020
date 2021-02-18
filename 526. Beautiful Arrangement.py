class Solution:
    def countArrangement(self, N: int) -> int:
        visited = [0]*(N+1)
        self.res = 0
        def backtrack(N, pos, visited):
            if pos > N: self.res += 1
            for i in range(1, N+1):
                if visited[i] == 0 and (pos%i == 0 or i%pos == 0):
                    visited[i] = 1
                    backtrack(N, pos + 1, visited)
                    visited[i] = 0
        backtrack(N, 1, visited)
        return self.res
    