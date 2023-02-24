def sorted(val1,val2):
    if val2 == "asc":
        val1.sort()
    elif val2 == "desc":
        val1.sort(reverse=True)
    return val1 

lst = [20,2,15]   
sorts = sorted(lst, "asc")
print(sorts)