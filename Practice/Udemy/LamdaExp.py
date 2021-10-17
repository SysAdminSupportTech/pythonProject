#using Map function
#Lamda expresssion is expected to be used once
def square(num):
    return num**2

square = lambda num: num ** 2
print(square(2))

my_nums = [1,2,3,4,5]
valist = list(map(lambda num: num ** 2, my_nums))
print(valist)
mynums = [1,2,3,4,5]
#using the filter function
print(list(filter(lambda num: num%2 == 0,mynums)))