from rectangle import *
import circle
from threed_graphics import cuboid, sphere

# Rectangle
l = 10
b = 5
print("Rectangle Area:", area(l, b))
print("Rectangle Perimeter:", perimeter(l, b))

# Circle
r = 5
print("Circle Area:", circle.area(r))
print("Circle Perimeter:", circle.perimeter(r))

# Cuboid
l = 10
b = 5
h = 4
print("Cuboid Area:", cuboid.area(l, b, h))
print("Cuboid Perimeter:", cuboid.perimeter(l, b, h))

# Sphere
r = 5
print("Sphere Area:", sphere.area(r))
print("Sphere Perimeter:", sphere.perimeter(r))