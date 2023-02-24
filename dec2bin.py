def dec2bin(decimals):
    remainders = []
    while decimals < 1024:
        v1 = decimals // 2      
        v2 = decimals % 2 
        if decimals != 0:
            decimals = v1 
            remainders.append(v2)           
            continue
        return remainders[::-1]


binary = dec2bin(7)
print(binary)