import random
import math

def monte_carlo_circle_area(radius, num_points):
    square_area = (2 * radius) ** 2
    inside_circle = 0
    
    for _ in range(num_points):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        
        if x**2 + y**2 <= radius**2:
            inside_circle += 1
    
    circle_area_estimate = (inside_circle / num_points) * square_area
    return circle_area_estimate

radius = 1 
num_points = 10000

estimated_area = monte_carlo_circle_area(radius, num_points)
print(f"Estimated area of the circle with radius {radius}: {estimated_area}")

actual_area = math.pi * radius**2
print(f"Actual area of the circle: {actual_area}")
print(f"Error: {abs(actual_area - estimated_area)}")
