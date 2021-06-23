#python program to sort list in Ascending order
numList = []
number = int(input("Please Enter the total number of List Element: "))
for i in range(1, number + 1):
    value = int(input("Please Enter the Value of %d Element: " %i))
    numList.append(value)
    numList.sort()
    print("Element After Sorting List in Ascending Order is : ", numList)