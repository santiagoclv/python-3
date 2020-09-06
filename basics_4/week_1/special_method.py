
import math

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)
    
    def __add__(self, otherPoint):
        """ It's posible to overrive the behavior an object has when it is presented to an operator """
        return Point(
            self.x + otherPoint.getX(),
            self.y + otherPoint.getY()
        )
    
    def __sub__(self, otherPoint):
        """ Same here but for the substraction """
        return Point(
            self.x - otherPoint.getX(),
            self.y - otherPoint.getY()
        )

a = Point(3, 4)
b = Point(5, 6)
print(a + b)
print(a - b)