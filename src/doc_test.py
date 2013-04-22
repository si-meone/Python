
def add(x, y):
    '''
    >>> add(2,4)
    7
    '''
    total = x + y
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()