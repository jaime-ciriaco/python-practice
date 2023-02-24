#The function should convert the radians into degrees and then return that value.
import math
def rad2deg(value):
    deg = value * (180/ (math.pi))
    return deg 

deg = rad2deg(2)
print(deg)

