class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            res = 0
            for col in range(n):
                if visitedCol[col] + visitedDiag1[row + col] + visitedDiag2[row - col] == 0:
                    visitedCol[col] = 1
                    visitedDiag1[row + col] = 1
                    visitedDiag2[row - col] = 1
                    if row == n - 1:
                        res += 1
                    else:
                        res += backtrack(row + 1)
                    visitedCol[col] = 0
                    visitedDiag1[row + col] = 0
                    visitedDiag2[row - col] = 0
            return res
        visitedCol = [0]*n
        visitedDiag1 = [0]*(2*n - 1)
        visitedDiag2 = [0]*(2*n - 1)
        return backtrack(0)