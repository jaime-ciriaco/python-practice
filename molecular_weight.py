def mole_weight():
    element = input("Enter element name: ")
    hydro_atoms = eval(input("Enter amount of hydrogen atoms: "))
    carbon_atoms = eval(input("Enter amount of carbon atoms: "))
    oxygen_atoms = eval(input("Enter amount of oxygen atoms: "))

    total_weight = (hydro_atoms * (1.0079)) + (carbon_atoms * (12.011)) + (oxygen_atoms * (15.9994))
    return "The total weight of " + element + " is " + str(total_weight)

print(mole_weight())


