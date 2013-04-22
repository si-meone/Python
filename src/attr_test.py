class attr_test(object):
    a = 'a'

if __name__ == '__main__':
    a1 = attr_test()
    a1 = attr_test()
    setattr(a1, 'a' , 'c')
    print a1.a
    