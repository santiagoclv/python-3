# Mutable

fruits = ['anana', 'banana', 'manzana', 'pera']
fruits[1:3] = ['naranja', 'durazno', 'tomate']

print(fruits)

# No Mutable
message = "Hello Word!"
message = "Pello Word!"
message[0] = "Y" # TypeError: 'str' object does not support item assignment

print(message)

