# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    for x in range(num, -1, -1):
        print(x)

num_count = (13)

countdown(num_count)



# Print and Return - Create a function that will receive a list with two
#  numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_ret(a,b):
    print(a)
    return b
print(print_and_ret(7,13))
    


# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


def add_first_and_length(a,b,c):
    return a + c
print(add_first_and_length(1,2,3))



# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


def greater_than_second(list):
    if len(list) < 2:
        return False
    listTwo = []
    for i in list:
        if i > list[1]:
            listTwo.append(i)
    print(len(listTwo))
    return listTwo

print(greater_than_second([6, 4, 3, 8, 10]))
print((greater_than_second([4])))




# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]


def size_and_val(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList

print((size_and_val(3,13)))