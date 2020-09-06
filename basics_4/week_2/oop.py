class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    # contructor
    def __init__(self, initX, initY):
        # atributs inicialization
        self.x = initX
        self.y = initY
    
    #Methods
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y


a = Point(1, 1)
b = Point(67, 67)

print(a.getX())
print(b.getX())

c = Point(1, 1)
prima = a
prima.setX(2)
a = Point(3, 3)

print(a is c)
print(a is prima)
print(a.getX(), prima.getX())