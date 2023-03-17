def fahrenheit():
    fahrenheit = eval(input("Enter fahrenheit temp: "))
    celsius = 5/9 * (fahrenheit - 32)
    return celsius

print(fahrenheit())