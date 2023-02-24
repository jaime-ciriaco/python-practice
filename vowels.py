def vowels(words):
    vowels = ['a','e','i','o','u']
    counter = 0 
    for letter in words:
        if letter in vowels:
            counter += 1
    return counter 
    
words = vowels("Beautiful")
print(words)