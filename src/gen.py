def lottery():
    x = 0
    while x < 6:
        yield x
        x += 1

l = lottery() 
print l.next() 
print l.next() 
