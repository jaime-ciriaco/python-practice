def stutter(word):
    return word[0:2] + "... " + word[0:2] + "... " + word + "?"

word = stutter("Blanca")
print(word)