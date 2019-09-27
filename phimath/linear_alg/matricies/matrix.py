import math

class Matrix:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.matrix = self.matrix[[0]*self.col_size] * self.row_size

    def get_row_size(self):
        return self.row_size
    
    def get_col_size(self):
        return self.col_size

    def get_val(self, row, col):
        value_mat = 0
        row_error = row if row < self.get_row_size() or row > self.get_row_size() else False
        col_error = col if col < self.get_col_size() or col > self.get_col_size() else False
        if row_error or col_error:
            raise ValueError("SELCTION_ERROR_PHI_MATH_MATRIX_VALUE")
        if not(row_error) or not(col_error):
            value_mat = self.matrix[row][col]
        return value_mat

    