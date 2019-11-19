from phimath.linear_alg.vectors.point2d import Point2D
from phimath.linear_alg.vectors.vector2 import Vec2
from phimath.linear_alg.matricies.matrix import Matrix
from phimath.linear_alg.matricies.matrix_operations import MatrixOperations

mat_one = Matrix(5, 5)
mat_two = Matrix(5, 5)
mat_two.set_matrix_value(2, 3, 1)
mat_one.set_matrix_value(2, 3, 230)
matrix_op = MatrixOperations(matrix_a=mat_one, matrix_b=mat_two)
added_mat = (matrix_op.add_mat())

print("Added mat value: " + str(added_mat.get_val(2, 3)))