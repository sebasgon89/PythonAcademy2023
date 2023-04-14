

# 1
# create a piece of code to trap an IndexError Exception

try:
    _list = [1, 2, 3]
    print (_list [3])
except IndexError as e:
    print (e)
    
# 2
# create a piece of code to trap an ArithmeticError Exception

try:
    _list = [1, 2, 3]
    print (len(_list)/0)
except ArithmeticError as e:
    print (e)


# 3
# create a piece of code to trap an TypeError Exception

try:
    "2" + 2
except TypeError as e:
    print (e)

# 4
# create a piece of code to trap an NameError Exception
try:
    _list = [1, 2, 3]
    print (llist)
except NameError as e:
    print (e)
    
# 5
# create a piece of code to trap an TypeError Exception
# and general exception

try:
    _list = [1, 2, 3]
    #_list + 2
    #_list[3]
except TypeError as e:
    print ("type error %s" % e)
except Exception as e:
    print ("general" + str(e))
