# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    result = []
    for item in some_list:
        if int(item) % 2 != 0:
            result.append(item)
    return result

all_odd([1,2,3,4,5,6,7,8])


# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    result = []
    for item in some_list:
        if int(item) % 2 == 0:
            result.append(item)
    return result

all_even([1,2,3,4,5,6,7,8])



# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    result = []
    for item in word_list:
        if len(item) >= 4:
            result.append(item)
    return result 


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = 0
    for item in some_list:
        if item < smallest:
            smallest = item
    return smallest
smallest([3,5,6,7,1])



# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = 0
    for item in some_list:
        if item > largest:
            largest = item
    return largest



# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    result = []
    for item in some_list:
        result.append(int(item) / 2)
    return result

halvesies([2,4,6,7])


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    result = []
    for item in word_list:
        result.append(len(item))
    return result



# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    suma = 0
    for item in numbers:
        suma = suma + int(item)
    return suma


# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    result = 1
    for item in numbers:
        result *= int(item)
    return result



# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""



# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    suma = 0
    sum_of_items = len(numbers)
    for item in numbers:
        suma += int(item)
    return avg





