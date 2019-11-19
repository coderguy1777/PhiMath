from phimath.linear_alg.matricies import matrix 

class MatrixOperations:
    def __init__(self, matrix_a=matrix.Matrix, matrix_b=matrix.Matrix):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def set_mat_a(self, mat_a=matrix):
        self.matrix_a = mat_a
    
    def set_mat_b(self, mat_b=matrix):
        self.matrix_b = mat_b

    def mult_mat(self):
        mat_a_rows = []
        mat_a_cols = []
        for i in range(len(self.matrix_a.row_size)):
            rows_val = [self.matrix_a.get_matrix_row(i)]
            mat_a_rows = [rows_val]
        
        for j in range(len(self.matrix_a.col_size)):
            col_vals = [self.matrix_a.get_matrix_column(j)]
            mat_a_cols = [col_vals]
        return mat_a_cols
