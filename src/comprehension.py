print '#=================================================================='
print 'a list comprehension'
print [i for i in xrange(1,11) if i % 2 == 0]

print '#=================================================================='
print 'a dictionary comprehension'
d = { 1:'a', 2:'b', 3:'c'}
print {key: value for key, value in d.iteritems()}
print '#=================================================================='

print '#=================================================================='
print 'a set comprehension'
l = [1,2,3,3,4,4,5,5,5,5,6,10]
print {i for i in l}
print '#=================================================================='

print '#=================================================================='
print 'a generator expression'
g = (a for a in [1,2,3])
print g.next(),; print g.next(),; print g.next()
print '#=================================================================='

print '#=================================================================='
print 'a generator function'
def countdown(n):
    print "Counting down from", n
    while n > 0:
        yield n
        n -= 1
x  = countdown(3
               )
print x.next(),;print x.next(),;print x.next(),;
print '#=================================================================='

