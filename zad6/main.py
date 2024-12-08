from geometry import Circle, Triangle, Square

circle = Circle(radius=5)
print(f"Circle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")

triangle = Triangle(a=3, b=4, c=5)
print(f"Triangle - Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter()}")

square = Square(side=4)
print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")
