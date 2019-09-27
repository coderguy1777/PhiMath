import math
from phimath.linear_alg.vectors.point2d import Point2D

class Vec2:
    def __init__(self, vec_pt=Point2D):
        self.vec_min = 0

    def add_vec2(self, vec_in_a=Point2D, vec_in=Point2D):
        vec_out = Point2D()
        vec_out.change_x(vec_in_a.get_x() + vec_in.get_x())
        vec_out.change_y(vec_in_a.get_y() + vec_in.get_y())
        return vec_out
    
    def sub_vec2(self, vec_in_a=Point2D, vec_in=Point2D):
        vec_out = Point2D()
        vec_out.change_x(vec_in_a.get_x() - vec_in.get_x())
        vec_out.change_y(vec_in_a.get_x() - vec_in.get_x())
        return vec_out
    
    def mult_vec2(self, vec_in_a=Point2D, vec_in=Point2D):
        vec_out = Point2D()
        vec_out.change_x(vec_in_a.get_x() * vec_in.get_x())
        vec_out.change_y(vec_in_a.get_x() * vec_in.get_x())
        return vec_out    
    
    def div_vec2(self, vec_in_a=Point2D, vec_in=Point2D):
        vec_out = Point2D()
        vec_out.change_x(vec_in_a.get_x() / vec_in.get_x())
        vec_out.change_y(vec_in_a.get_x() / vec_in.get_x())
        return vec_out

    def vec_mag(self, vec_mag=Point2D):
        return math.sqrt(math.pow(vec_mag.get_x()) + math.pow(vec_mag.get_y()))
