# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
exercise_string = "This is a string"
exercise_number = 1
exercise_list = ["Dogs", "Cats", "Birds"]
exercise_boolean = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
new_string = exercise_string[:3]
print(new_string) 

# Exercise 3: Use an index to grab the first element from your list.
first_element = exercise_list[0]
print(first_element)

# Exercise 4: Create a new number variable that adds 10 to your original number.
new_number = exercise_number + 10
print(new_number)

# Exercise 5: Use an index to get the last element in your list.
last_item = exercise_list[-1]
print(last_item)

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(",")
print(list_of_names)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase.
# Create a new string that takes the uppercase word and the rest of the original string.
uppercase_first_word_index = exercise_string.index(' ')
uppercase_first_word = exercise_string[0:uppercase_first_word_index].upper()
new_string = uppercase_first_word + exercise_string[uppercase_first_word_index:]
print(new_string)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
string_interpolation_exercise = f'The number I have chosen is {exercise_number}'
print(string_interpolation_exercise)

# Exercise 9: Print “hello world”.
print("hello world")

# Además necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena.
# Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
cadena = "Hola, ésta es la cadena del ejercicio."
word = cadena.find("Hola")
cadena = cadena.replace("Hola", "adiós")
print(cadena)