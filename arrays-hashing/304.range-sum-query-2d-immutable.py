# @leet start
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefix = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                above = self.prefix[i - 1][j] if i - 1 >= 0 else 0
                left = self.prefix[i][j - 1] if j - 1 >= 0 else 0
                diag = self.prefix[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
                self.prefix[i][j] = above + left - diag + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        diag = self.prefix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        above = self.prefix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        return total - above - left + diag

    def getSum(self, row, col):
        if 0 <= row < self.m and 0 <= col < self.n:
            return self.prefix[row][col]
        return 0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @leet end

