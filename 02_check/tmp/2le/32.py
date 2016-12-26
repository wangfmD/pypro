# codint:utf-8

the_count = [11, 21, 31, 4, 5]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
fruits = ['apples', 'oranges', 'pears', 'apricots']

for number in the_count:
    print "The is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r " % i

elememts = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elememts.append(i)

for i in elememts:
    print "Elememt was %d" % i
