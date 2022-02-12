#https://github.com/developer234/pythonProject/issues/13
#https://www.youtube.com/watch?v=JNXmCOumNw0&t=300s
import random
from Words import word
#def for words
def word_dic():
    game_word = random.choice(word)
    return game_word

#def for hangman
def hangman():
    pass

#Def for play
def play():
    puzzle_giver = 'Ealbert'
    player = ''
    wrong_guess = 6
    lettergussed = ""
    wrong_letter = 0

    player_name = input("Welcome to our Hangmang game. Please enter your name: ")
    print("Welcome {}".format(player_name))
    player = player_name
    secrete_word = word_dic()
    print(secrete_word)
    word_guess_length = len(secrete_word)#length of the guess word
    word_guide_dash = " _ " * word_guess_length

    while wrong_guess > 0 :
        user_guess = input("Guess a word for the game: ").upper()
        if user_guess in secrete_word.upper():
            print(f"You guess the letter '{user_guess}' is included.")
        else:
            print(f"Now word like {user_guess} found in the secrete word. ")
            wrong_guess -= 1


        lettergussed = lettergussed + user_guess
        for letter in secrete_word:
            if letter in lettergussed:
                print(letter, end="")
            else:
                print("_", end="")
                wrong_letter +=1
        
        if wrong_letter == 0:
            print("Congratulation, you have won the game. The secrete word is '{}'", format(secrete_word))
            break
    else:
        print("Sorry you did not win, try again...")
    

print(play())