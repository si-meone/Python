name = 'G'

def A():
    global name
    name = 'A'
    def B():
        #nonlocal
        name = 'B'
        


if __name__ == '__main__':
    A()
    print name