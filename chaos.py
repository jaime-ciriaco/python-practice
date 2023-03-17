def chaos():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many values should I print?: "))
    print("Input : ", x, " ", y)
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("    ", x, "    ", y )
    return "All values printed!"

ran_gen = chaos()
print(ran_gen)

