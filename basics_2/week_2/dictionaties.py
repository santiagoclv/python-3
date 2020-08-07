# Dictionary definition {key: value}
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}

eng2sp['four'] = 'cuatro'
eng2sp['five'] = 'cinco'
eng2sp['six'] = 'seis'

print(eng2sp)
for key in eng2sp:
    print(key, eng2sp[key]) # prints everithing as tuples, very strange

# Remove elements from a dictionary
print(len(eng2sp))
del eng2sp['four']
# Without Four
print(len(eng2sp))


# 
# 
# GET KEYS, VALUES AND ITEMS AS AN ARRAY OF TUPLES
print('keys', eng2sp.keys())
print('values', eng2sp.values())
print('items as tuples', eng2sp.items())

# Use of IN for cheking for existence

print('four' in eng2sp)
print('six' in eng2sp)


# Do not throw errors on getting values

print(eng2sp.get('four')) # get None
print(eng2sp.get('four', 4)) # setup a default value, insted of getting None, we will get 4
# print(eng2sp['four']) # Throw KeyError



#
# Aliasing in dictionaries
#

fruits = { 'banana': 'banana', 'apple': 'manzana', 'peach': 'durazno'}
alias = fruits

alias['banana'] = 'bonano'

print(fruits)



##
## Acumulator pattern with dictonaries
##

board_file = open("../week_1/board.txt", "r")
board_data = board_file.read()
character_count = {}
for c in board_data:
    if(character_count.get(c) == None):
        character_count[c] = 0

    character_count[c] += 1
print(character_count)
board_file.close()

# UPDATE method
# If does not exist it will be created and if it exists it will be updated with the new value.

character_count.update({"z": 23})
character_count.update({"T": 23})


# counting characters and looking for the max frequencies

sally = "sally sells sea shells by the sea shore"

characters = {}
for ch in sally:
    characters.update({ch: characters.get(ch, 0) + 1})

max_value = max(characters, key=lambda k: characters[k]) # max(characters.values())
best_char = ''
for key, value in characters.items():
    if(value == max_value):
        best_char = key
        break