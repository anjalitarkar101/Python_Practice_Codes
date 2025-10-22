# Create a function that takes the radius of a circle as a parameter and returns both 
# its circumference and area.

import math

def circle_stats(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference , area

result1 , result2 = circle_stats(5)
print("Circumference:", result1 ,  "Area:", result2)