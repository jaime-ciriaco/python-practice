def future_value():
    principal = eval(input("Enter amount to invest each year: "))
    rate = eval(input("Enter the interest rate: "))
    years = eval(input("Enter number of years of investment: "))
    period = eval(input("Enter the number of times interest is compounded each year: "))


    for i in range(years * period):
        total_amount = principal * (1 + rate/ period)
    return "The value in " + str(years) + " years is: " + str(total_amount)

futval = future_value()
print(futval)

