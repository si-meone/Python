def f(x):
    print 'in f'
    print 'x is {}'.format(x)
    print

def g(x, y):
    print 'in g'
    print 'x is {}'.format(x)
    print 'y is {}'.format(y)
    print

def h(x, *args):
    print 'in h'
    print 'x is {}'.format(x)
    print 'args is {}'.format(args)
    print

def i(x, y, *args, **kwargs):
    print 'in i'
    print 'x is {}'.format(x)
    print 'y is {}'.format(y)
    print 'args is {}'.format(args)
    print 'kwargs is {}'.format(kwargs)
    print
    
if __name__ == '__main__':
    f(1)
    g(y=2, x=1)
    h(1, 2, 3, 4)
    i(x=1, y=2, 3,  a=5 )