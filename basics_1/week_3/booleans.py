# apart from the clasic Logic operators, in Python there are a couple more operators

print('a' in 'apple')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple')

print('x' not in 'apple')
print('apple' not in 'apple')
print('' not in 'a')
print('' not in 'apple')


# Also I could use it for arrays, but works different it compare to the whole element. 
# Lets say that this is same as strings if we take strings as an array of characters

print('apple' not in ['apple1', 'apple2' , 'apple3', 'apple4'])
print('apple2' not in ['apple1', 'apple2' , 'apple3', 'apple4'])


# PRECEDENCE OF OPERATORS


# 1 Parenthesis
# 2 Power - Due to some historical quirk, an exception to the left-to-right left-associative rule is the exponentiation operator **
# 3 Multiplication
# 4 Addition

# 4.5 AND & OR

# 5 Left to Right

