
# Catching exceptions using try and except

# convert Fº into Cº

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')


if 6 == 6:
    print("Hola")