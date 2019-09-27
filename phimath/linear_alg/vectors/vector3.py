from phimath.linear_alg.vectors.point3d import Point3D
import math

class Vec3:
    def __init__(self, vec=Point3D):
        self.vec = vec
        self.mult_vec = lambda vec_x=Point3D, vec_y=Point3D : vec_x.get_x() * vec_y.get_x() + vec_x.get_y() * vec_y.get_y() + vec_x.get_z() * vec_y.get_z()
        self.add_vec = lambda vec_x=Point3D, vec_y=Point3D : vec_x.get_x() + vec_y.get_x() + vec_x.get_y() + vec_y.get_y() + vec_x.get_z() + vec_y.get_z()
        self.div_vec = lambda vec_x=Point3D, vec_y=Point3D : vec_x.get_x() / vec_y.get_x() + vec_x.get_y() / vec_y.get_y() + vec_x.get_z() / vec_y.get_z()
        self.sub_vec = lambda vec_x=Point3D, vec_y=Point3D : vec_x.get_x() + vec_y.get_x() + vec_x.get_y() + vec_y.get_y() + vec_x.get_z() + vec_y.get_z()

    def sub_vec3d(self, vecb=Point3D):
        self.vec = self.sub_vec(self.vec, vecb)
        return self.vec.get_group()

    def add_vec3d(self, vecb=Point3D):
        self.vec = self.add_vec(self.vec, vecb)
        return self.vec.get_group()

    def div_vec3d(self, vecb=Point3D):
        self.vec = self.div_vec(self.vec, vecb)
        return self.vec.get_group()

    def dot_product(self, vecb=Point3D):
        self.vec = self.mult_vec(self.vec, vecb)
        return self.vec.get_group()
    
    def mult_scalar(self, scalar):
        self.vec.change_x(self.vec.get_x() * scalar)
        self.vec.change_y(self.vec.get_y() * scalar)
        self.vec.change_z(self.vec.get_z() * scalar)
        return self.vec.get_group()

    def div_scalar(self, scalar):
        self.vec.change_x(self.vec.get_x() * scalar)
        self.vec.change_y

    def vec_mag(self):
        return math.sqrt(pow(self.vec.get_x(), 2) + pow(self.vec.get_y(), 2) + pow(self.vec.get_z(), 2))
    
    def vec_to_unit_vec(self, mag):
        return Vec3(self.vec.get_x()/mag, self.vec.get_y()/mag, self.vec.get_z()/mag)

    def unit_vec_mag(self, mag):
        return math.sqrt(pow(self.vec.get_x()/mag, 2) + pow(self.vec.get_y()/mag, 2) + pow(self.vec.get_z()/mag, 2))
