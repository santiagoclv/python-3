"""
    indefinite iteration ----> because in diff of for we do not know how many time we are going to iterate. 
"""

def sum_to(a_bound):
    """ Return the sum of 1+2+3 ... n """

    the_sum  = 0
    a_number = 1
    while a_number <= a_bound:
        the_sum += a_number
        a_number += 1
    return the_sum

print(sum_to(4))

print(sum_to(1000))


## The Listener Loop

theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)


# break and continue

"""
    break: breaks the iteration.
    continue: jump from its line to the next iteration.
"""

x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
    if x == 10:
        """In case something goes wrong"""
        break
print("Done with our loop! X has the value: " + str(x))
