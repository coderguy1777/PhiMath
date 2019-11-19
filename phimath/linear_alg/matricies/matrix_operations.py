from phimath.linear_alg.matricies import matrix

class MatrixOperations:
    def __init__(self, matrix_a=matrix.Matrix, matrix_b=matrix.Matrix):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def get_mat_a(self):
        return self.matrix_a

    def get_mat_b(self):
        return self.matrix_b

    def add_mat(self):
        resultant_matrix = matrix.Matrix(self.matrix_a.get_row_size(), self.matrix_a.get_col_size())
        if self.matrix_a.get_row_size() != self.matrix_b.get_row_size() or self.matrix_a.get_col_size() != self.matrix_b.get_col_size():
            raise ValueError("ERROR: MATRIX VALUES OF UNLIKE DIMENSIONS")
        else:
            for i in range(resultant_matrix.get_row_size()):
                for j in range(resultant_matrix.get_col_size()):
                    result_add = self.matrix_a.get_val(i, j) + self.matrix_b.get_val(i, j)
                    print(str(result_add))
                    resultant_matrix.set_matrix_value(i, j, result_add) 

        return (resultant_matrix)


    def sub_mat(self): 
        resultant_matrix = matrix.Matrix(self.matrix_a.get_row_size(), self.matrix_b.get_col_size())
        if self.matrix_a.get_row_size() != self.matrix_b.get_row_size() or self.matrix_a.get_col_size() != self.matrix_b.get_col_size():
            raise ValueError("ERROR: MATRIX VALUES OF UNLIKE DIMENSIONS")
        else: 
            for i in range(resultant_matrix.get_row_size()): 
                for j in range(resultant_matrix.get_col_size()): 
                    result_sub = self.matrix_a.get_val(i, j) - self.matrix_b.get_val(i, j)
                    resultant_matrix.set_matrix_value(i, j, result_sub)

        return (resultant_matrix)

    def div_mat(self): 
        resultant_matrix = matrix.Matrix(self.matrix_a.get_row_size(), self.matrix_a.get_row_size())
        if self.matrix_a.get_row_size() != self.matrix_b.get_row_size() or self.matrix_a.get_col_size() != self.matrix_b.get_col_size(): 
            raise ValueError("ERROR: MATRIX VALUES OF UNLIKE DIMENSIONS")
        else: 
            for i in range(resultant_matrix.get_row_size()): 
                for j in range(resultant_matrix.get_col_size()):
                    result_div = self.matrix_a.get_val(i, j) / self.matrix_b.get_val(i, j)
                    resultant_matrix.set_matrix_value(i, j, result_div)

        return (resultant_matrix)