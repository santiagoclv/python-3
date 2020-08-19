
"""
    'sort' method or 'sorted' function iterate over collections and by default sort them in ascending order.

    It could take 2 key parameters: key and reverse
        key: let you setup the function that takes the value to be evalueted
        reverse: let you specify if the collection should be sorted in descending order

    def sort|sorted(colection, *, key, reverse)

"""

# reverse

L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))

# key function

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

# or in reverse order
print(sorted(L1, reverse=True, key=absolute))



## Sorting dictionaries


dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary, key= lambda k: dictionary[k], reverse=True)


## Sorting tupples
# It is compared value by value in every tupple

tups = [('A', 3, 2),
        ('A', -1, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]
for tup in sorted(tups):
    print(tup)

# ('A', -1, 2)
# ('A', 2, 4)
# ('A', 3, 2)
# ('B', 3, 1)
# ('C', 1, 2)
# ('C', 1, 4)

# Tuples are super usefull there there is an object and ypu want
# to sort them by multiple properties: This is posible using the key parameter 
# with a lambda function and returning a tupple with the order of the properties to evaluate.

