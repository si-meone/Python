class Shape(object):
    def __init__(self, position, colour=None, size=0):
        self.x, self.y = position
        self.colour = colour
        self.size = size

    def __str__(self):
        pass

    def _getsize(self):
        pass

    def _setsize(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width, position):
        super(Rectangle, self).__init__(position)
        self.height , self.width = height, width
        self.size = width
        
    def __str__(self):
        return 'type={} x={} y={} colour={} size={} height={}'.format(
                self.__class__.__name__, self.x, self.y, self.colour,
                self.size, self.height)

    def _getsize(self):
        return (self.height, self.width)

    def _setsize(self, value):
        (self.height, self.width) = value


class Square(Rectangle):

    def __init__(self, height, position):
        super(Square, self).__init__(height, height, position)
    
    def __str__(self):
        return 'type={} x={} y={} colour={} size={} height={}'.format(
                self.__class__.__name__, self.x, self.y, self.colour,
                self.size, self.height)

    def _getsize(self):
        return self.length

    def _setsize(self):
        pass


class Oval(Shape):
    def __init__(self, diameter1, diameter2):
        super(Oval, self).__init__()
        self.diameter1 = 0
        self.diameter2 = 0

    def _getsize(self):
        return self.diameter1

    def _setsize(self, diameter1):
        pass
    
if __name__ == '__main__':
    rectangle = Rectangle(2, 4, (0, 0))
    print rectangle

    square = Square(2, (1, 1))
    print square

#  
#class Circle(Oval):
#    def __init__(self, width, length):
#        super(Square, self).__init__(width, length)
#        self.diameter1
#
#    def _getsize(self):
#        pass
#
#    def _setsize(self):
#        pass

