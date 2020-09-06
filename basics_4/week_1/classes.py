
import math

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
    
    def __str__(self):
        """ This is another especial method, thats why uses the undeerscore before and after the name  __nombre__ """
        return "x = {}, y = {}".format(self.x, self.y)
    
    def distanceFromOrigin(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))


def distance(point1, point2):
    """ Function to get the distance between to points objects """
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

def halfway(point_a, point_b):
        mx = (point_a.getX() + point_b.getX())/2
        my = (point_a.getY() + point_b.getY())/2
        return Point(mx, my)

p = Point(4,3)
q = Point(0,0)
print(distance(p,q))


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
print(a, b, c, prima)
print("distanceFromOrigin a, prima, b: ",a.distanceFromOrigin(), prima.distanceFromOrigin(), b.distanceFromOrigin())

print("halfway a, b", halfway(a, b))
