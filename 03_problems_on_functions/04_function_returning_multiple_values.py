# Create a function that takes the radius of a circle as a parameter and returns both 
# its circumference and area.

##### Parameter: A variable defined in the function definition.
##### Argument: The actual value passed to the function when it is called.

import math                    # Importing math module to use mathematical constants and functions

def circle_stats(radius):                     # radius is a parameter
    circumference = round(2 * math.pi * radius, 3)
    area = round(math.pi * radius ** 2, 3)
    return circumference , area

result1 , result2 = circle_stats(6)            # 6 is an argument
print("Circumference:", result1 ,  "Area:", result2)