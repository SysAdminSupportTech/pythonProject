def myyoda(text):
    wordlist = text.split()
    reversed_word_list = wordlist[::-1]
    return reversed_word_list

print(' '.join(myyoda("i am home")))