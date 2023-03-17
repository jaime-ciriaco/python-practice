def convert():
    #celsius = eval(input("What is the Celsius temperature? "))
    #print("The temperature is ", fahrenheit, " degrees Fahrenheit.")
    for i in range(0,101,10):
        fahrenheit = 9/5 * i + 32 
        print("Celsius temp is ", i,"C and Fahrenheit temp is ", fahrenheit)
    return "All done!"


fahrenheit = convert()
print(fahrenheit)