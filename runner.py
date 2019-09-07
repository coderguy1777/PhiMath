import phimath.linear_alg.translate_vector as vc
from phimath.vectors.point2d import Point2D

b = Point2D(8, 8)
a = vc.Vec(0.5, 0.5)
for i in range(0, 100):
    a.trans_x()
    print(str(a.get_x()))
    b.get_group()
print(str(b.get_group()))