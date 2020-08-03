largest = None
smallest = None

def min(value, smallest):
    if smallest is None or value < smallest:
        smallest = value
    return smallest

def max(value, largest):
    if largest is None or value >= largest:
        largest = value
    return largest


while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        smallest = min(num, smallest)
        largest = max(num, largest)
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

