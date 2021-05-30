# Given a 2D matrix matrix, find the sum of the elements inside the rectangle de
# fined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#  
# 
#  Implement the NumMatrix class: 
# 
#  
#  NumMatrix(int[][] matrix) initializes the object with the integer matrix matr
# ix. 
#  void update(int row, int col, int val) updates the value of matrix[row][col] 
# to be val. 
#  int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the 
# elements of the matrix array inside the rectangle defined by its upper left corn
# er (row1, col1) and lower right corner (row2, col2). 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["NumMatrix", "sumRegion", "update", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 
# 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
# Output
# [null, 8, null, 10]
# 
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8
# numMatrix.update(3, 2, 2);
# numMatrix.sumRegion(2, 1, 4, 3); // return 10
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 200 
#  -105 <= matrix[i][j] <= 105 
#  0 <= row < m 
#  0 <= col < n 
#  -105 <= val <= 105 
#  0 <= row1 <= row2 < m 
#  0 <= col1 <= col2 < n 
#  At most 104 calls will be made to sumRegion and update. 
#  
#  Related Topics Binary Indexed Tree Segment Tree 
#  👍 511 👎 66


# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.n = self.row*self.col
        matrix_1d = []
        if self.n > 0:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix_1d.append(matrix[i][j])
            self.tree = self.buildTree(matrix_1d)

    def update(self, row: int, col: int, val: int) -> None:
        pos = self.col*row + col + self.n
        self.tree[pos] = val
        while pos > 0:
            pos = pos//2
            self.tree[pos] = self.tree[pos*2] + self.tree[pos*2 + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.col*row1 + col1
        right = self.col*row2 + col2
        res = 0
        while left <= right:
            if left%2 == 1:
                res += self.tree[left]
                left += 1
            if right%2 == 0:
                res += self.tree[right]
                right -= 1
            left = left//2
            right = right//2
        return res

    def buildTree(self, matrix):
        tree = [0]*self.n*2
        for i in range(self.n):
            tree[i+self.n] = matrix[i]
        for i in range(self.n-1, 0, -1):
            tree[i] = tree[i*2] + tree[i*2+1]
        return tree

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)
