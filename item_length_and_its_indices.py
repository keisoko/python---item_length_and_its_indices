from my_python_modules import operate

"""Logs item and its indices with the integer thousand separator""" 
def item_and_its_indices(item):
    for index, value in enumerate(item):
        print(f"index[{index}] = {value:,}") if type(value) == int else print(f"index[{index}] = {value}")


"""Logs length of the given item"""
def item_length(item):
    length = len(item)
    if type(item) == str:
        print(f"The length of the given string is {length}")
    if type(item) == list:
        print(f"The length of the given list is {length}")
    if type(item) == dict:
        print(f"The length of the given dictionary is {length}")


"""invokes higher order functions for the given type of item"""

my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

operate(item_and_its_indices, my_list)
operate(item_length, my_list)


string = "The Master and Margarita"

operate(item_and_its_indices, string)
operate(item_length, string)