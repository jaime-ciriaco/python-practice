def fact():
    n = eval(input("Enter value to compute: "))
    factorial = 1 
    for i in range(n):
        factorial = factorial * (i+1) 

    return factorial

print(fact())

