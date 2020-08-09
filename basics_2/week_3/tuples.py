""" 
    Tuples are very useful whenever we want to pass or return multiple values to and from a function.

    Packing and Unpacking tuples
"""

# paking

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# or equivalently
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia[4], type(julia))

def add(a, b):
    return a+b, a, b # What is equivalently to return (a + b, a, b)



# Unpacking

name, surname, birth_year, movie, movie_year, profession, birth_place = julia
print(name, surname, birth_year, movie, movie_year, profession, birth_place)

result, param_a, param_b = add(1, 2)
print(result, param_a, param_b)

# unpacking into iterators

authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)

"""
    Python way of iterate over list values using its index: enumerate a build-in function that returns a tuple with ( index, value )
"""
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)


# unpacking into arguments of a function

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked
