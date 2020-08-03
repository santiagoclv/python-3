# Because of the definition of and
# the short-circuit behavior leads to a clever technique called the guardian pattern.

x = 6
y = 2
x >= 2 and (x/y) > 2

x = 1
y = 0
x >= 2 and (x/y) > 2

x = 6
y = 0
x >= 2 and (x/y) > 2 # error ZeroDivisionError: division by zero. This would be fixed if there was an additional part where we check if y == 0