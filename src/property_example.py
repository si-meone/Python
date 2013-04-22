class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print "I'm the 'x' property."
        return self._x

    @x.setter
    def x(self, value):
        print "I'm the setting 'x' property."
        self._x = value

    @x.deleter
    def x(self):
        print "I'm the deleting 'x' property."
        del self._x


if __name__ == '__main__':
    print 'test' 
    c = C()
    c.x
    c.x = 'test'
    del c.x