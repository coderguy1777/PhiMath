from phimath.vectors.point3d import Point3D
class Vec3:
    def __init__(self, vec=Point3D):
        self.vec = vec
        # simple "overloads" for easy code
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
    
    def vec_scalar(self, scalar):
        self.vec.change_x(self.vec.get_x() * scalar)
        self.vec.change_y(self.vec.get_y() * scalar)
        self.vec.change_z(self.vec.get_z() * scalar)
        return self.vec.get_group()
