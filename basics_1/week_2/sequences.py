my_hardware = ["mouse", "keywords"]
my_hardware.append("wacom")
# concatenation
extra_hardware = [ "headphones", "spekers" ]

my_hardware += extra_hardware

print("Everything", my_hardware)
print("Sound", my_hardware[3:])

# strings are inmutable but arrays are not

# Tuples! => they are not mutables as the arrays

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

print(type(julia))
print(type(my_hardware))


# With negative index acxesors
# these are the same!
print("negative index, sound", my_hardware[-2: 14])
print("negative index, sound", my_hardware[-2:])
print("no sound", my_hardware[:-2])


# Repetition 

alist = [1,3,5]
print(alist * 3)

# Count: The method then returns the number of times that the argument occured in the string/list the method was used on.

alist = alist * 3
print("How many 4?", alist.count(4))
print("How many 1?", alist.count(1))

# index returns the leftmost index where the argument is found.

try:
    print("Where is 4?", alist.index(4)) # ValueError 4 not found!
except ValueError:
    pass

print("Where is 3?", alist.index(3))

# Split: ny default it split strings by blank space
song = "The rain in Spain..."
wds = song.split()
print(wds)

wds_by_e = song.split('e')
print(wds_by_e)


# Inverse method to split: join!

glue = 'e'
print(glue.join(wds_by_e))

# manera rebuscada y erronea de recorrer un array
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])



# DELETE ELEMENTS!

fruits = ['anana', 'banana', 'manzana', 'pera']
fruits[3: ] = ['naranja', 'durazno', 'tomate']
print(fruits)
del fruits[0]
print(fruits)
del fruits[1:3]
print(fruits)

# No Mutable