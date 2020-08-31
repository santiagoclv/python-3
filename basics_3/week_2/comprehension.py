""" List Comprehension is the Python way to do map and filter operations over lists. """

## MAP

numeros = [2, 4, 5, 6, 7]
doble_pares = map(lambda num: num * 2, numeros)

# Now the Comprehension way

doble_pares_v2 = [ num * 2 for num in numeros]

print(doble_pares, doble_pares_v2)


## FILTER

solo_pares = filter(lambda num: num % 2 == 0, numeros)

# Now the Comprehension way

solo_pares_v2 = [ num for num in numeros if num % 2 == 0 ]

print(solo_pares, solo_pares_v2)


## This is a powerfull tool, this let us combine map with filter operations in one instruction

doble_solo_pares = [ num * 2 for num in numeros if num % 2 == 0 ]
print(doble_solo_pares)


# Using help from functions

def doble(numero):
    return numero * 2

def es_par(numero):
    return numero % 2 == 0

doble_solo_pares_set = { doble(num) for num in numeros if es_par(num) } # this will generate a set
doble_solo_pares_dictionary = { num: doble(num) for num in numeros if es_par(num) } # this will generate a dictionary
doble_solo_pares_generador = ( doble(num) for num in numeros if es_par(num) ) # this will generate a generator

# All kind of iterators.
print(doble_solo_pares, type(doble_solo_pares), "doble_solo_pares list")
for num in doble_solo_pares:
    print(num)
print(doble_solo_pares_set, type(doble_solo_pares_set), "doble_solo_pares set")
for num in doble_solo_pares_set:
    print(num)
print(doble_solo_pares_dictionary, type(doble_solo_pares_dictionary), "doble_solo_pares dictionary")
for key in doble_solo_pares_dictionary:
    print(key, doble_solo_pares_dictionary[key])
print(doble_solo_pares_generador, type(doble_solo_pares_generador), "doble_solo_pares generador")
for num in doble_solo_pares_generador:
    print(num)