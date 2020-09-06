class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

class Vegetable():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return len(self.name)

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20), Fruit("Potato", 10), Fruit("Carrot", 25), Fruit("Sweet Potato", 21)]

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority(), reverse=True):
    print(f.name)