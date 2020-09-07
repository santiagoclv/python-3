from random import randrange

class Pet:
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name

    def greet(self):
        return 'Hi, I\'m {}'.format(self.name)
    
    def feed(self):
        return self.sounds[randrange(len(self.sounds))]

class Cat(Pet):
    sounds = ['Meow']

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        print("Arf! Thanks!")
        return super().feed()
        

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        super().__init__(name) # call the parent class's constructor
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def greet(self):
        return 'Hi, I\'m {}'.format(self.name) * self.chirp_number

perro = Dog("Rodolfo")
gato = Cat("Pelandro")
pajaro = Bird("Agusto", 5)

print(perro.greet())
print(gato.greet())
print(pajaro.greet())

print(perro.feed())
print(gato.feed())
print(pajaro.feed())