def nodes(lsts, n1,n2):
    return lsts[n1][n2]

lst =[
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

for node1 in lst:
    for node2 in node1:
        print(node2)

connected = nodes(lst, node1, node2)
print(connected)

