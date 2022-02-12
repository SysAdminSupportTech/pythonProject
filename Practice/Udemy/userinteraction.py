#Display Function
game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

#Position Choice
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice=input("Pick a position(0,1,2): ")
        if choice not in ['0','1','2']:
            print("sorry, invalid Choice Selected")
    return int(choice)

#position_choice()
def replacement_value(game_list, position):
    user_placement = input("Type a string to place a position: ")
    game_list[position] = user_placement
    return game_list
#print(replacement_value(game_list, 1))

#Game on Choice
def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice=input("Keep Playing? (Y or N): ")
        if choice not in ['Y','N']:
            print("sorry, i dont understand, please choose Y or N")
    if choice == "Y":
        return True
    else:
        return False
#print(gameon_choice())

game_on =True
game_list = [0,1,2]

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_value(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()