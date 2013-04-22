from timeit import Timer
##    t = Timer("'hello' + 'world'")
#    print '1', timeit('print "hello"')
#    t = Timer("join_string2('hello', 'world')", "from __main__ import join_string2")
#    print '2', t.timeit()

    
#def join_string2(s1, s2):
#    pass
#    t = Timer("join_string2('hello', 'world')", "from __main__ import join_string2")
#    print '2', t.timeit()


s1, s2 = 'a', 'b'
s3 = ''.join(s1 + s2)
print s3
