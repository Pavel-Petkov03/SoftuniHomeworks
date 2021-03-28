from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        bigger_y = self.y if self.y > y else y
        smaller_y = self.y if self.y < y else y
        smaller_x = self.x if self.x < x else x
        bigger_x = self.x if self.x > x else x
        cord_y = bigger_y - smaller_y
        cord_x = bigger_x - smaller_x
        return sqrt(cord_x ** 2 + cord_y ** 2)


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
a = 5
n = 4

