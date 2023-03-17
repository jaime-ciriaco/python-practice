def miles():
    kilometer = eval(input("Please enter kilometer distance: "))
    miles = kilometer * 0.62

    return "The conversion kilometers to miles is: " + str(miles)

print(miles())