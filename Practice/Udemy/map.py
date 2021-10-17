#using Map function
#Map expect a function to work. this iterate only functions
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

#to get a list
vallis = list(map(square, my_nums))
#print(vallis)
