import math
from phimath.linear_alg.vectors.point2d import Point2D

class Vec2:
    def __init__(self, vec_pt=Point2D):
        self.vec_pt = vec_pt

    def add_vec2(self, vec_in_a=Point2D):
        self.vec_pt.change_x(self.vec_pt.get_x() + vec_in_a.get_x())
        self.vec_pt.change_y(self.vec_pt.get_y() + vec_in_a.get_y())
        return self.vec_pt.get_group()
    
    def sub_vec2(self, vec_in_a=Point2D):
        self.vec_pt.change_x(self.vec_pt.get_x() + vec_in_a.get_x())
        self.vec_pt.change_y(self.vec_pt.get_y() + vec_in_a.get_y())
        return self.vec_pt.get_group()
    
    def mult_vec2(self, vec_in_a=Point2D):
        self.vec_pt.change_x(self.vec_pt.get_x() * vec_in_a.get_x())
        self.vec_pt.change_y(self.vec_pt.get_y() * vec_in_a.get_y())
        return self.vec_pt.get_group()
    
    def div_vec2(self, vec_in_a=Point2D):
        self.vec_pt.change_x(self.vec_pt.get_x() * vec_in_a.get_x())
        self.vec_pt.change_y(self.vec_pt.get_y() * vec_in_a.get_y())
        return self.vec_pt.get_group()
    
    def add_scalar(self, scalar):
        self.vec_pt.change_x(self.vec_pt.get_x() + scalar)
        self.vec_pt.change_y(self.vec_pt.get_y() + scalar)
        return self.vec_pt.get_group()

    def sub_scalar(self, scalar):
        self.vec_pt.change_x(self.vec_pt.get_x() - scalar)
        self.vec_pt.change_y(self.vec_pt.get_y() - scalar)
        return self.vec_pt.get_group()

    def mult_scalar(self, scalar):
        self.vec_pt.change_x(self.vec_pt.get_x() * scalar)
        self.vec_pt.change_y(self.vec_pt.get_y() * scalar)
        return self.vec_pt.get_group()

    def div_scalar(self, scalar):
        self.vec_pt.change_x(self.vec_pt.get_x() * scalar)
        self.vec_pt.change_y(self.vec_pt.get_y() * scalar)
        return self.vec_pt.get_group()

    def vec_mag(self, vec_mag=Point2D):
        return math.sqrt(math.pow(vec_mag.get_x()) + math.pow(vec_mag.get_y()))

    def vec2_to_unit2_vec(self, mag):
        self.vec_pt.change_x(self.vec_pt.get_x()/mag)
        self.vec_pt.change_y(self.vec_pt.get_y()/mag)
        return self.vec_pt.get_group()

    def vec_angle(self, vec_a=Point2D):
        return math.tanh(vec_a.get_y()/vec_a.get_x())