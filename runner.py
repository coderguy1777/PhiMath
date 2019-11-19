from phimath.linear_alg.vectors.point2d import Point2D
from phimath.linear_alg.vectors.vector2 import Vec2
from phimath.linear_alg.matricies.matrix import Matrix
from phimath.linear_alg.matricies.matrix_operations import MatrixOperations

mat_one = Matrix(5, 5)
for i in range(mat_one.get_row_size()):
    for j in range(mat_one.get_row_size()):
        print(mat_one.matrix[i][j