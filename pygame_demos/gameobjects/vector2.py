import math

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = 1.0 * value

    def __str__(self):
        return f"({self.x}, {self.y})"

    def from_points(P1, P2):
        return Vector2(P2[0] - P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        magnitude = self.get_magnitude()
        try:
            self.x /= magnitude
            self.y /= magnitude
        except ZeroDivisionError:
            self.x = 0
            self.y = 0

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)


# A = (10.0, 20.0)
# B = (30.0, 35.0)
# C = (15.0, 45.0)
#
# AB = Vector2.from_points(A, B)
# BC = Vector2.from_points(B, C)
# AC = Vector2.from_points(A, C)
# print("Vector AB", AB)
# print(AB.get_magnitude())
#
# print("Vector AC", AC)
#
# print("AB + BC is", AB + BC)
#
# # AB.normalize()
# # print(AB)
#
# step = AB * 0.1
# position = Vector2(*A)
# for n in range(10):
#     position += step
#     print(position)