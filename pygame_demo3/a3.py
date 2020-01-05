from gameobjects.vector3d import Vector3

A = (-6, 2, 2)
B = (7, 5, 10)
plasma_speed = 100 #meters / second
AB = Vector3.from_points(A, B)
print(f"Vector to droid is {AB}")

distance_to_target = AB.get_magnitude()
print(f"Distance to droid is {distance_to_target} meters")

plasma_heading = AB.get_normalised()
print(f"Heading is {plasma_heading}")