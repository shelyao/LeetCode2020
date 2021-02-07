class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row = 0):
            for col in range(n):
                if visited_col[col] + visited_diag1[row + col] + visited_diag2[row-col] == 0:
                    queens.add((row, col))
                    visited_col[col] = 1
                    visited_diag1[row + col] = 1
                    visited_diag2[row-col] = 1
                    solution = []
                    if row == n - 1: 
                        for _, col in sorted(queens):
                            solution.append('.'*col+'Q'+'.'*(n-col-1))
                        res.append(solution)
                    else:
                        backtrack(row + 1)
                    queens.remove((row, col))
                    visited_col[col] = 0
                    visited_diag1[row + col] = 0
                    visited_diag2[row-col] = 0
        visited_col = [0]*n
        visited_diag1 = [0]*(2*n - 1)
        visited_diag2 = [0]*(2*n - 1)
        res = []
        queens = set()
        backtrack()
        return res
                    