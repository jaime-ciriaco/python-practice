import math 
def sphere(radius):
    volume = 4/3 * math.pi * radius**3
    area = 4 * math.pi * radius**2
    return "The volume of the sphere is " + str(volume) + " and area is " + str(area)

radius = eval(input("Enter radius value: "))
print(sphere(radius))