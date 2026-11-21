square = lambda a: a*a
rectangle = lambda l, b: l*b
triangle = lambda b, h: 0.5*b*h
a = float(input("Enter square side:"))
l = float(input("Enter rectangle length:"))
b = float(input("Enter rectangle breadth:"))
base = float(input("Enter triangle base:"))
h = float(input("Enter triangle height:"))
print("Area of square:", square(a))
print("Area of rectangle:", rectangle(l, b))
print("Area of triangle:", triangle(base, h))