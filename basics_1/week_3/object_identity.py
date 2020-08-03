a = "banana"
b = "banana"

# is -> Logic operator that says if a variable has the same identity as other.
# very useful for objects.


print(a is b) # True -> because they point to the "same" string .

print(a == b) # True -> because their value is equal


a_array = ["banana", "naranja"]
b_array = ["banana", "naranja"]

# is -> Logic operator that says if a variable has the same identity as other.
# very useful for objects.


print(a_array is b_array) # False -> because they are 2 diffents objects

print(a_array == b_array) # True -> because their value is equal

###########################################
# id() give us the id that identify the object pointed by the variable

print(id(a)) 

print(id(b))

print(id(a_array))

print(id(b_array))

###################################
# References of objects by Aliasing

a = [81,82,83]
b = [81,82,83]
# Are different objects
print(a is b)

# Now the thow variables point to the same object
b = a
print(a == b) # compare them by value
print(a is b) # compare them by identity

b[0] = 5
print(a)


###############################
# Cloning objects (Arrays)

a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b) # True
print(a is b)  # FALSE

b[0] = 5

print(a)
print(b)


