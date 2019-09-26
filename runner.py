from phimath.linear_alg.vectors.point2d import Point2D
from phimath.linear_alg.vectors.vector2 import Vec2

b = Point2D(8, 8)
a = Vec2(0.5, 0.5)
for i in range(0, 100):
    a.trans_x()
    print(str(a.get_x()))
    b.get_group()
print(str(b.get_group()))