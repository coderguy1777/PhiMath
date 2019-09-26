import math

class Matrix:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.matrix = self.matrix[self.row_size][self.col_size]