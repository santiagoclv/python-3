# Built-in functions

max('Hello world') # 'w'
min('Hello world') # ' '
len('Hello world') # 11

int(-2.3)
float('3.14159')
str(32)

import math

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))

import random

for i in range(10):
    x = random.random()
    print(x)

random.randint(5, 10) # number between 5 and 10, both included

t = [1, 2, 3]
random.choice(t) # choice ramndom item from t



# Define functions!

def say_hi(name):
    print('Hi', name, '!')

say_hi("Roberto")

def addtwo(a, b):
    added = a + b
    return added

# Void functions return None
print(type(say_hi)) # <class 'function'>
print(type(say_hi("Roberto"))) # <class 'NoneType'>
print(type(None)) # <class 'NoneType'>


# Assigment

def computepay(hrs,rate):
    extra_hrs = 0
    if hrs > 40:
        extra_hrs = hrs - 40
        hrs -= extra_hrs
    return hrs * rate + extra_hrs * rate * 1.5    

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print("Pay",p)