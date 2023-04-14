# now, we create a simple function, without parameters

def one():
    print ("first function")


#call the function 3 times!
one()
one()
one()

# take a look to the next piece of code:

print("We start message")

def message():
    print("message! ")

message()

print("We end here.")

#now, what is wrong here? (un comment and check...)

#hi()
#
#def hi():
#    print("hi!")
#

# we add the parameters...

def two(param):
    print ("hello '%s'" % param)

two("juan")
two("ana")


# possitional parameters!

def three(name, lastname):
    print ("--> he/she is '%s, %s'" %(name, lastname))

three("Ana", "Gomez")
three("Juan", "Perez")

# keyword argument passing

three(lastname='Rodriguez', name='Diego')
three(name='Paula', lastname='Oliva')
three('James', lastname='Bond')
# error! -->> three('Bond', name='James') # raise a syntax Error!!

# pre-define a values

def four(initial, end=10):
    print ("initial+end = %s" % (initial+end,))

four(4)
four(4, 5)
four(initial=90, end=2)

# the return instruction

def five(val=False):
    return val

print("five result '%s'" % five())
print("five result '%s'" % five(True))
print("five result '%s'" % five(False))


def six(param=0):
    if param>0:
        print ("es mayor")
        param = 0
    elif param<0:
        print ("es menor")
        param = 0

    print ("param %s" % param)

six(10)
six(-10)
six()
six(0)

        



