def user_value():
    choice = 'WRONG'
    while choice.isdigit() == False:
        choice = input("Enter a number in the range of (0-10): ")
        if choice.isdigit() == False:
            print("Sorry You enter the wrong value")
    return int(choice)

user_value()