# 1. Countdown - Create a function that accepts a number as an input. Return a new
# list that counts down by one, from the number (as the 0th element) down to 0 
# (as the last element).

def countdown(num):
    newList = []
    for num in range(num, -1, -1):
        newList.append(num)
    return newList

print(countdown(10))

# 2. Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second.

def printAndReturn(list):
    print(list[0])
    return(list[1])

printAndReturn([5,10])

# 3. First Plus Length - Create a function that accepts a list and returns the sum of
# the first value in the list plus the list's length.

def firstPlusLength(list):
    sum = list[0] + len(list)
    return sum

print(firstPlusLength([1,2,3,4,5,6,7,8,9,10]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a
# new list containing only the values from the original list that are greater than its
# 2nd value. Print how many values this is and then return the new list. If the list
# has less than 2 elements, have the function return False

def valuesGreaterThanSecond(list):
    newList = []
    count = 0
    if len(list) < 2:
        return False
    for i in range(len(list)):
        if list[1] < list[i]:
            newList.append(list[i])
            count+=1
    print(f"Count: {count}")
    return newList

myList = valuesGreaterThanSecond([1, 6, 2, 3, 4, 5, 7, 8, 9, 10])
print(myList)

#  5. This Length, That Value - Write a function that accepts two integers as
# parameters: size and value. The function should create and return a list whose
# length is equal to the given size, and whose values are all the given value.

def thisLengthThatValue(length, value):
    newList = []
    for num in range(length):
        newList.append(value)
    return newList

myList = thisLengthThatValue(5, 7)
print(myList)