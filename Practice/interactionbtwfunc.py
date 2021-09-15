import random
example = [1,2,3,4,5,6,7,8]
mylist = ['','0','']
def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist
#result = shuffle_list(example)
#result = shuffle_list(mylist)
#print(result)


def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a Number: 0, 1, 2 :")

    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == '0':
        print("Correct!")
    else:
        print("Wrong guess")
        print(mylist)

mylist = ['','0','']
guess = player_guess()
mixedupvalue = shuffle_list(mylist)
check_guess(mixedupvalue,guess)