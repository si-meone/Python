def contains_even_number(l):
    "Prints whether or not the list l contains an even number."
    for elt in l:
        if elt % 2 == 0:
            print "list contains an even number"
            break
    else:
        print "list does not contain an even number"
    pass

if __name__ == '__main__':
#    contains_even_number([1])
    contains_even_number([])