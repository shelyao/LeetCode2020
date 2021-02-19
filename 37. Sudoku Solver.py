class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        colDict = [defaultdict(int) for _ in range(9)]
        rowDict = [defaultdict(int) for _ in range(9)]
        boxDict = [defaultdict(int) for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = int(board[i][j])
                    boxIdx = self.getBoxIdx(i, j)
                    rowDict[i][x] = 1
                    colDict[j][x] = 1
                    boxDict[boxIdx][x] = 1
        def fill(row, col, colDict, rowDict, boxDict):
            nextRow =row + (col + 1)//9
            nextCol = (col + 1)%9
            if row == 9: return True
            boxIdx = self.getBoxIdx(row, col)
            nextBoxIdx = self.getBoxIdx(nextRow, nextCol)
            #print(row, col)
            if board[row][col] != '.':
                return fill(nextRow, nextCol, colDict, rowDict, boxDict)
            for i in range(1, 10):
                if colDict[col][i] + rowDict[row][i] + boxDict[boxIdx][i] == 0:
                    board[row][col] = str(i)
                    colDict[col][i] = 1
                    rowDict[row][i] = 1
                    boxDict[boxIdx][i] = 1
                    if fill(nextRow, nextCol, colDict, rowDict, boxDict): 
                        return True
                    colDict[col][i] = 0
                    rowDict[row][i] = 0
                    boxDict[boxIdx][i] = 0
                    board[row][col] = '.'
            return False
        fill(0, 0, colDict, rowDict, boxDict)
        return board
                    
    def getBoxIdx(self, row, col):
        return 3*(row//3) + col//3
                    