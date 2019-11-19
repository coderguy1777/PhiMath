import math

class Matrix:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.matrix = [[0 for x in range(row_size)] for y in range(col_size)]

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
        else:
            value_mat = self.matrix[row][col]
        return value_mat
    
    def get_matrix_row(self, row):
        row_vals = []
        if row > self.get_row_size():
            raise ValueError("ROW_VAL_ERROR")
        else:
            for i in range(row):
                row_vals.append(self.matrix[i][0])
        return row_vals
    
    def get_matrix_column(self, col):
        col_vals = []
        if col > self.get_col_size():
            raise ValueError("COL_VAL_ERROR")
        else:
            for i in range(col):
                col_vals.append(self.matrix[0][i])
        return col_vals
    
    def set_matrix_value(self, row, column, value):
        if row > self.get_row_size() or column > self.get_col_size():
            raise ValueError("ROW SELECTION IS TOO BIG, OR COLUMN SELETION")
        else:
            print("Matrix values for mat set.")
            self.matrix[row][column] = value
        