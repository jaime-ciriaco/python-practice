# Write a function in Python that accepts two numeric parameter.
# The first will be a list of numbers. 
# The second parameter will be a string that can be one of the following values: asc, desc, and none.
# If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. 
# If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered. 
#val1 = [20,9,5]
def sorted(val1,val2):
    if val2 == "asc":
        val1.sort()
        return val1
    elif val2 == "desc":
        val1.sort(reverse=True)
        return val1
    elif val2 == "none":
        return val1
    else:
        print("All done!")

lst = [20,2,15]   
sorts = sorted(lst, "none")
print(sorts)

