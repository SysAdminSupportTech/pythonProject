#print true if the next number are the same in a list
def has_33(num):
    for i in range(0,len(num) -1):
        if num[i] == 3 and num[i+1] == 3:
            return True
    return False
print(has_33([1,3,3]))


#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def  paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result
print(paper_doll("hello"))