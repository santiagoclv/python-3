# strings are array of character, as in everywhere

fruit = 'banana'
first_character = fruit[0]
print('fruit', fruit)
print('first_character', first_character)

# length of an array
fruit_name_len = len(fruit)

# It's an array, so you could loop them

for letter in fruit:
    print(letter)


# Slicing Strings/Arrays

print("From 0 up to 3 but not included:", fruit[0:3])

print("From 3 up to 20 characters more:", fruit[3:24])

print("From 0 up to 24 characters more:", fruit[:24])

print("From 3 up to whatever:", fruit[3:])

print("Everything:", fruit[:])


# String comparition: You could use == < > to sort words in alfabeting order

# IndexError: error you get when trying to get a part of the array does not exist

try:
    print(fruit[24])
except IndexError:
    print('IndexError: Todo mal, posible solution: fruit[24:25]')


# dir: a useful function that let us know what an object is capable of, returns an array

print(dir(24))
print(dir("Hello"))

# Strings in Python can be enclosed in either single quotes (') or double quotes ("), or three of each (''' or """)

print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
print("""This message will span
several lines
of the text.""")

