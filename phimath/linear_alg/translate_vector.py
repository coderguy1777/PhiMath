import math
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def trans_y(self):
        self.y = self.y + 1
    def trans_x(self):
        self.x = self.x + 1
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y