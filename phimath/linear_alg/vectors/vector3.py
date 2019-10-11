from phimath.linear_alg.vectors.point3d import Point3D
import math

class Vec3:
    def __init__(self, vec=Point3D):
        self.vec = vec
    
    def sub_vec3d(self, vecb=Point3D):
        self.vec.change_x(self.vec.get_x() - vecb.get_x())
        self.vec.change_y(self.vec.get_y() - vecb.get_y())
        self.vec.change_z(self.vec.get_z() - vecb.get_z())
        return self.vec.get_group()

    def add_vec3d(self, vecb=Point3D):
        self.vec.change_x(self.vec.get_x() + vecb.get_x())
        self.vec.change_y(self.vec.get_y() + vecb.get_y())
        self.vec.change_z(self.vec.get_z() + vecb.get_z())
        return self.vec.get_group()

    def div_vec3d(self, vecb=Point3D):
        self.vec.change_x(self.vec.get_x() / vecb.get_x())
        self.vec.change_y(self.vec.get_y() / vecb.get_y())
        self.vec.change_z(self.vec.get_z() / vecb.get_z())
        return self.vec.get_group()

    def mult_vec3d(self, vecb=Point3D):
        self.vec.change_x(self.vec.get_x() * vecb.get_x())
        self.vec.change_y(self.vec.get_y() * vecb.get_y())
        self.vec.change_z(self.vec.get_z() * vecb.get_z())
        return self.vec.get_group()

    def sub_scalar(self, scalar):
        self.vec.change_x(self.vec.get_x() - scalar)
        self.vec.change_y(self.vec.get_y() - scalar)
        self.vec.change_z(self.vec.get_z() - scalar)
        return self.vec.get_group()

    def add_scalar(self, scalar):
        self.vec.change_x(self.vec.get_x() + scalar)
        self.vec.change_y(self.vec.get_y() + scalar)
        self.vec.change_z(self.vec.get_z() + scalar)
        return self.vec.get_group()
    
    def mult_scalar(self, scalar):
        self.vec.change_x(self.vec.get_x() * scalar)
        self.vec.change_y(self.vec.get_y() * scalar)
        self.vec.change_z(self.vec.get_z() * scalar)
        return self.vec.get_group()

    def div_scalar(self, scalar):
        self.vec.change_x(self.vec.get_x() / scalar)
        self.vec.change_y(self.vec.get_y() / scalar)
        self.vec.change_z(self.vec.get_z() / scalar)
        return self.vec.get_group()

    def vec_mag(self):
        return math.sqrt(pow(self.vec.get_x(), 2) + pow(self.vec.get_y(), 2) + pow(self.vec.get_z(), 2))
    
    def vec_to_unit_vec(self, mag):
        self.vec.change_x(self.vec.get_x()/mag)
        self.vec.change_y(self.vec.get_y()/mag)
        self.vec.change_z(self.vec.get_z()/mag)
        return self.vec.get_group()

    def unit_vec_mag(self, mag):
        return math.sqrt(pow(self.vec.get_x()/mag, 2) + pow(self.vec.get_y()/mag, 2) + pow(self.vec.get_z()/mag, 2))
