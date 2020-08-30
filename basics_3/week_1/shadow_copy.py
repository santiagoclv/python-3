original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original) # Their ids are different
print(copied_version == original) # Tehy have the same content
original[0].append(["canines"]) # now in the first place of the array will have ['dogs', 'puppies', ["canines"]]
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)  # It will look the same as "original" because it's a shadow coppy, not a deep copy
