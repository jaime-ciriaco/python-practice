def thunder(time):
    distance = 1100 * time
    return "The distance based on time elapsed between the flash and sound of thunder is: " + str(distance) + " feet"

time = eval(input("Enter the  time in (seconds) you heard the thunder up to it striked: "))
print(thunder(time))