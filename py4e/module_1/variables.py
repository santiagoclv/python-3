x = 345
print(x, "HOLA")
print(type('Hello, World!'), type(x), type(3434.23), type(3434.23))

minute = 20 + 5
hour = 1
total_minutes = hour*60+minute
total_hours_trunked = minute//60
total_hours = minute/60
total_hours_remainder = minute/60
area_cuadrada = 5**2
area_cuadrada = area_cuadrada - 5

quotient = 7 // 3
print(quotient)
remainder = 7 % 3
print(remainder)

print(total_minutes, total_hours, area_cuadrada, total_hours_remainder, total_hours_trunked)


# Operator: Rules of precedence

# 1 Parenthesis
# 2 Power - Due to some historical quirk, an exception to the left-to-right left-associative rule is the exponentiation operator **
# 3 Multiplication
# 4 Addition
# 5 Left to Right

# Example
1 + 2 ** 3 / 4 * 5
1 + 8 / 4 * 5
1 + 2 * 5
1 + 10
11

# Example
1 + 2 ** (3 / 4) * 5
1 + 2 ** 0.75 * 5
1 + 1.681792830507429 * 5
1 + 8.408964152537145
9.408964152537145

# String concat and repete

first = '100'
second = '150'
print(first + second) # 100150

first = 'Test '
second = 3
print(first * second) # Test Test Test

# Input from keyword

prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt) # if I set as input "asdad"
int(speed) + 5 # I'll get < ValueError: invalid literal for int() with base 10: 'asdad' >

# Type conversion

print(float(99), 'is a float')
print(float('99'), 'also is a float')
print(int('1'), 'is an integer')
print(str(float('99')), 'is a string')
