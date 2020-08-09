""" Using reduce, map and filter"""

from functools import reduce

# REDUCE

product = reduce((lambda x, y: x * y), [1, 2, 3, 4], 0)

# FILTER

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# MAP

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

num_medals = map(lambda item : item[1], gold.items())