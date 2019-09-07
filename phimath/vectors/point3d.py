class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def change_x(self, new_x):
        self.x = new_x
    def change_y(self, new_y):
        self.y = new_y
    def change_z(self, new_z):
        self.z = new_z
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
    def get_group(self):
        return list(self.get_x(), self.get_y(), self.get_z())