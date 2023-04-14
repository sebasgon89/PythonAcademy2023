# LAB TIME!

# 1
# Design a function that returns true if the month passed by parameter
# is the last month of the year, or returns how many months remain
# to end the year

def func1(param=12):
    if type(param) != int:
        print ("Error in type")
        return False

    if param == 12:
        return True
    elif param > 12:
        print ("greater than 12")
        return False
    else:
        return 12 - param
    
    

print (func1("hola"))
print (func1(10)) #--> returns 2
print (func1(11)) #--> returns 1
print (func1(1))  #--> returns 11
print (func1(12)) # --> returns True
ret = func1(5)
print (ret)


# 2
# Design a function that takes a parameter, called month, and
# returns the number of days in that month.
# For example, parameter "january" return "31", parameter "april" return 30

print ("\n" * 4)

def func2(month="enero"):
    meses = { "enero" : 31,
              "febrero": 28,
              "marzo": 31,
              "abril": 30,
              "mayo": 31,
              "junio": 30,
              "julio": 31,
              "agosto": 31,
              "septiembre": 30,
              "octubre": 31,
              "noviembre": 30,
              "diciembre": 31}

    if type(month) != str:
        print ("Error in type")
        return 0

    if month in meses.keys():
        return meses[month]
    else:
        print ("valor no es un mes")
        return 0
    
    

    
print(func2("enero"))    # returns --> 31
print(func2("marzo"))    # returns --> 31
print(func2("febrero"))  # returns --> 28
print(func2("junio"))    # returns --> 30
print(func2("tractor"))  # returns --> 0
print(func2(12))         # returns --> 0


# 3
# Design a function that takes 3 parameters.
# You need to check if they are integers.
# If they are not, it must return None.
# If they are all 3 integers, return the
# power between them.

print ("\n" * 4)

def func3(a, b, c):

    if type(a) == type(b) == type(c) == int:
        return a ** b ** c
    else:
        return None 

print (func3(1,2,3))
print (func3(1,2,"a"))
print (func3(1,"2",3))
print (func3(1,2,3))

# 4
# Design a function with 3 parameters and
# returns this parameters into a tuple

print ("\n" * 4)

def four(p1, p2, p3, p4):
    return (p1, p2, p3, p4)

a, b, c, d = four (1, 2, 3, 4)
print ("a %s - b %s - c %s - d %s" % (a, b, c, d))
x = four (1,2,3,4)
print(type(x))
print(x)
