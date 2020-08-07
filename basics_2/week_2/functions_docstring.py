# Definition + docstring (documentation of a module, function or class)
def drawSquare():
    """Make turtle t draw a square of with side sz."""
    print("Hola, soy una funcion")

print(drawSquare.__doc__)
print(__doc__) # this module
drawSquare()


# Parameters: They are pass as reference,
# but if we use de = sing it would not change de reference for the object outside de function.

uno = 1
dos = [2]
tres = [3]
cuatro = { "custro": 4 }
cinco = (5)

def do_things(one, two, three, four, five):
    two = ["two"]
    three.append("three")
    four["cienco"] = 5
    five = (5)
    print(one, two, three, four, five)
    print(id(one), id(two), id(three), id(four), id(five))

print(uno, dos, tres, cuatro, cinco)
print(id(uno), id(dos), id(tres), id(cuatro), id(cinco))
do_things(uno, dos, tres, cuatro, cinco)
print(uno, dos, tres, cuatro, cinco)

# A function always will return something, None at last.

def add(a, b):
    return a + b

def show_add(a, b):
    print(a + b)

print(add(4, 5))
print(show_add(4, 5))