# The WHILE statement

n = 5
while n > 0:
    print(n)
    n -= 1
print('Blastoff!')


# We could use "break" to stop the execution of the body loop

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# When you are in an iteration of a loop and want to finish the current iteration and immediately jump to the next iteration

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


# The FOR statement

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')




# built-in max and min functions make wrintting this functions unnecessary

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)


smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
