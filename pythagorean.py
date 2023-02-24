def check_pthagorean(lst):
    if (lst[0]) ** 2 + (lst[1]) ** 2 == (lst[2]) ** 2:
        return "List has a pythagorean triplet"
    else:
        return "List does not have pythagorean"

lst = [0,4,5]

checking = check_pthagorean(lst)
print(checking)