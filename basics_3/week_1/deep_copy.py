import copy

original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]

shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original) # This is the way a deep copy is made

original.append("Hi there")
original[0].append(["marsupials"])

print("-------- Original -----------")
print(original)
print("-------- shallow copy -----------")
print(shallow_copy_version)

print("-------- deep copy -----------")
print(deeply_copied_version)
