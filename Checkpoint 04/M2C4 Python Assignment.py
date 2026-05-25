# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
from decimal import Decimal
import math

exercise_list = ["Cats", "Dogs", "Birds"]
exercise_tuple = ("Cats", "Dogs", "Birds")
exercise_float = 42.42
exercise_integer = 67
exercise_decimal = Decimal(10.42) #this is a float now
exercise_dictionary = {
    "Cats" : "Dogs",
    "Dogs" : "Cats",
    "Birds" : "Snakes",
    "Snakes" : "Birds",
}

print("Exercise 1")
print("This is a list: ")
print(exercise_list)
print("This is a tuple: ")
print(exercise_tuple)
print("This is a float: ")
print(exercise_float)
print("This is an integer: ")
print(exercise_integer)
print("This is a decimal number: ")
print(exercise_decimal)
print("This is a dictionary: ")
print(exercise_dictionary)

# Exercise 2: Round your float up.
rounded_up_float = math.ceil(exercise_float)
print("Exercise 2")
print(rounded_up_float)

# Exercise 3: Get the square root of your float.
square_root_of_float = math.sqrt(exercise_float)
print("Exercise 3")
print(square_root_of_float)

# Exercise 4: Select the first element from your dictionary.
first_element_of_dictionary = list(exercise_dictionary.items())
print("Exercise 4")
print(first_element_of_dictionary[0])

# Exercise 5: Select the second element from your tuple.
print("Exercise 5")
print(exercise_tuple[1])

# Exercise 6: Add an element to the end of your list.
print("Exercise 6")
exercise_list.append("Crocs")
print(exercise_list)

# Exercise 7: Replace the first element in your list.
print("Exercise 7")
exercise_list[0] = "Crabs"
print(exercise_list)

# Exercise 8: Sort your list alphabetically.
print("Exercise 8")
exercise_list.sort()
print(exercise_list)

# Exercise 9: Use reassignment to add an element to your tuple.
print("Exercise 9")
exercise_tuple += ("Bees",)
print(exercise_tuple)