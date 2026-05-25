# Cree un bucle For de Python.
print("Ejercicio 1) Bucle for")
animals = ["Cats", "Crocs", "Snakes", "Birds"]
for animal in animals:
    print(f"I really like {animal}.")

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
print("\nEjercicio 2) Suma en Python")
def suma(arg_1, arg_2, arg_3):
    print(f"La suma es: {arg_1} + {arg_2} + {arg_3} = {arg_1 + arg_2 + arg_3}")
    return arg_1 + arg_2 + arg_3

suma(6, 13, 27)

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
print("\nEjercicio 3) Suma lambda en Python")
suma_lambda = lambda arg_1, arg_2, arg_3 : arg_1 + arg_2 + arg_3
total = suma_lambda(6, 13, 27)
print(f"La suma lambda es: {total}")

#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
# *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
print("\nEjercicio 4) Encontrando el valor dentro de una lista")
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for nombre in lista_nombre:
    if nombre == "Enrique":
        print("Hemos encontrado a Enrique en la lista, así que dejamos de buscarlo.")
        break
    print(f"Estamos buscando a Enrique pero aquí sólo hemos encontrado a {nombre}")