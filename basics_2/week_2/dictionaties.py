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

