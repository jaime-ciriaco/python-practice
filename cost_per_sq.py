import math
def cost(total_cost, r):
    total_area = math.pi * r**2
    cost_per_square_inch = total_cost / total_area
    return "The total cost per square inch of a pizza is: $" + str(cost_per_square_inch) 

total_cost = eval(input("Enter total cost: "))
r = eval(input("Enter radius: "))

print(cost(total_cost, r))

