import math
def circle_or_square(radius, area):
    circumference = 2 * math.pi * radius
    perimeter = math.sqrt(area) * 4
    if circumference > perimeter:
        return True 
    else:
        return False
    
shape = circle_or_square(8,144)
print(shape)

