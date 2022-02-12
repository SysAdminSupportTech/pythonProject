word = "secrete"
guesses = []
done = False

while not done:
    for letter in guesses:
        if letter.lower() in guesses:
            print(letter, end = " ")
        else:
            print("_", end=" ")
    done = True