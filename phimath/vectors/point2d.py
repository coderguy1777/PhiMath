class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def change_x(self, new_x):
        self.x = new_x
    def change_y(self, new_y):
        self.y = new_y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_group(self):
        return list([self.get_x(), self.get_y()])