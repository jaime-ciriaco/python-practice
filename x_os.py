def xs(word):
    x_counter = 0 
    o_counter = 0 
    for letter in word:
        if letter == "x":
            x_counter += 1
        elif letter == "o":
            o_counter += 1 
    
    if x_counter != o_counter:
        return False 
    elif x_counter == o_counter:
        return True
    else:
        return True 

    
words = xs("orlando")
print(words)