import math

from gameobjects.matrix44 import Matrix44

identity = Matrix44()
print(identity)

p1 = (1.0, 2.0, 3.0)
p2 = identity.transform(p1)

print(p2)
print(identity.get_column(2))

translation = Matrix44.translation(10, 5, 2)
print(translation)

scale = Matrix44.scale(2.0)
print(scale)

s = scale.transform(p1)

print(s)

z_rotate = Matrix44.z_rotation(math.radians(-45))
print(z_rotate)

a = (0, 10, 0)
b = z_rotate.transform(a)
print(b)

translation1 = Matrix44.translation(5, 10, 2)
translation2 = Matrix44.translation(-7, 2, 4)
print(translation1 * translation2)

translation = Matrix44.translation(5, 10, 0)
rotate = Matrix44.y_rotation(math.radians(45))
translation_rotate = translation * rotate

print(translation_rotate)
