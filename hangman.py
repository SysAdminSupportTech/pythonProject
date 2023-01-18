#!/usr/bin/python3
import time
import random

"""
This is a hangman code. The game is usually played with two players onboard. One the guesser and the other, the question provider"
"""
#Two players are involved
#Provide the word to guess
#The guesser of the word provided.
#How the game is played. 
# The provider of word pick a word from the pool of words in his mind, and provide a dash equivalent to the word he want the guesser to guess.
#The wrong guessing build ups the hangman

def game_instruction():
    print("How to play the Hangma game\n\n")
    print("This game requires a two persons to play.\nThe Owner of the game suggest a word, and you as the player is expected to guess that word within the space of five (5) guesses\nif not then the owner of the game won.")



player_name = input("Welcome, my name is Crawler, i'm happy to meet you. Please Enter your name: ")
print("Welcome {}".format(player_name))
print(" ") #empty space
how_to_play = input("Do you want the instruction on how to play the game (y/n): ")
usrinput_how_to_play = how_to_play.lower()
if(usrinput_how_to_play == 'y'):
    game_instruction()

#Body of the main game
#Select a random number from the group of words in a list
random_words = ['school','church','mosque','house','dull']
group_of_random_word = random.choice(random_words)
print(group_of_random_word)

#Get the lenght of the random number selected
word_selected_lenght = len(group_of_random_word) 

#Game Start
counter = 1
wrong_guess = []
correct_guess = []
print("Let start. You have 8 guesses to get the work correctly\n")
while counter <= 8:
    time.sleep(1)
    user_guessed = input("Guess my secrete word. Note: My Secrete word is {} in lenght:  ".format( word_selected_lenght))
    user_placeString = list(word_selected_lenght * "_") #Create a list of dash based on the lenght of the word selected
    if user_guessed in group_of_random_word:
        word_index_value = group_of_random_word.index(user_guessed) #Getting the index value from the word selected and delete it from the word



        #Find the character in the group of word and print it out, for the other words, replace them with an underscore (_)

    else:
        print("You are wrong!!!")
        wrong_guess.append(user_guessed)
        print(wrong_guess)
    
    counter += 1



