# Boolean expressions
print('5 == 5', ' is True', 'Type: ', type(5 == 5)) # True
print('5 == 6', ' is False', 'Type: ', type(5 == 5)) # True

x = 5 == 5
y = 5 == 6

# Boolean operators 

x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
x is y               # x is the same as y
x is not y           # x is not the same as y

# Logical operators 

# and, or, not

x > 0 and x < 10 
2%2 == 0 or 1%3 == 0
not (x > y)

# Comment: Any nonzero number is interpreted as “True”

# If Logic

sunny = True

if sunny :
    print("It's a sunny day")

## If-else Logic

if sunny :
    print("It's a sunny day")
else :
    print("It's not a sunny day")

## If-elif-else Logic

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


## Assigments

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
extra_hrs = 0
if hrs > 40:
    extra_hrs = hrs - 40
    hrs -= extra_hrs

print(hrs * rate + extra_hrs * rate * 1.5)


###

score = float(input("Enter Score: "))

if score > 1 or score < 0:
    print('Score out of range')
    quit()

if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')