# Triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is", area)

# Square
side = float(input("Enter the side of the square: "))
area = side * side
print("The area of the square is", area)

# Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is", area)

# Parallelogram
base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
area = 0.5 * base * height
print("The area of the parallelogram is", area)

# Trapezoid (US)
base1 = float(input("Enter the base of the trapezoid (US): "))
base2 = float(input("Enter the base of the trapezoid (US): "))
height = float(input("Enter the height of the trapezoid (US): "))
area = 0.5 * (base1 + base2) * height
print("The area of the trapezoid (US) is", area)

# Trapezium (UK)
base1 = float(input("Enter the base of the trapezium (UK): "))
base2 = float(input("Enter the base of the trapezium (UK): "))
height = float(input("Enter the height of the trapezium (UK): "))
area = 0.5 * (base1 + base2) * height
print("The area of the trapezium (UK) is", area)

# Circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print("The area of the circle is", area)

# Ellipse
major_axis = float(input("Enter the length of the major axis of the ellipse: "))
minor_axis = float(input("Enter the length of the minor axis of the ellipse: "))
area = 3.14 * major_axis * minor_axis
print("The area of the ellipse is", area)

# Sector
radius = float(input("Enter the radius of the sector: "))
angle = float(input("Enter the angle of the sector: "))
area = 0.5 * radius * radius * angle / 360
print("The area of the sector is", area)