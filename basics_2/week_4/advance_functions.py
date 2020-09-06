
"""
 There are two tricky things that can confuse you with default values. 
 The first is that the default value is determined at the time that 
 the function is defined, not at the time that it is invoked. 
"""

# Optional Parameters
initial = 7
def f(x, y =3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

f(2)
initial = 10
f(2, 5)
f(2, 5, 8)

"""
    Another warning:
    The second tricky thing is that if the default value is set to a mutable object, such as a list or 
    a dictionary, that object will be shared in all invocations of the function. 
    This can get very confusing, so I suggest that you never set a default value that
     is a mutable object. For example, follow the exceution of this one carefully.
"""

def ff(a, L=[]):
    L.append(a)
    return L

print(ff(1)) # initial values: 1, []
print(ff(2)) # initial values: 2, [1]
print(ff(3)) # initial values: 3, [1, 2]
print(ff(4, ["Hello"])) # initial values: 4, ["Hello"]
print(ff(5, ["Hello"])) # initial values: 5, ["Hello"]

"""
    Keyword Parameters: with keyword-based parameter passing. This is particularly convenient when there are 
    several optional parameters and you want to provide a value for one of the later parameters while not providing a value for the earlier ones.

    https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments


    The use case will determine which parameters to use in the function definition:
"""
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument


# Mixing everything
# *arguments would be a tuple and **keywords would be a dictionary

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
        
"""
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

    As guidance:

    Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

    Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

    For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.
"""




# Keyword parameters on .format

names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
