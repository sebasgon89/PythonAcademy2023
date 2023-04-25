ejemplo1
 
Python
# LAB TIME!
# 1
# Design a function that returns true if the month passed by parameter
# is the last month of the year, or returns how many months remain
# to end the year

def last_month(m):
    if (m < 12):
        return  (12 - m)
    elif (m == 12):
        return True
    else:
        return False
        
# print(last_month(2))
# print(last_month(12))
# 2
# Design a function that takes a parameter, called month, and
# returns the number of days in that month.
# For example, parameter "january" return "31", parameter "april" return 30

def days_month(m):
    if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        return 31
    elif  (m==4 or m==6 or m==9 or m==11):
        return 30
    elif (m==2)
        if bisiesto(y): return 29 else: return 29
    
    
# 3
# Design a function that takes 3 parameters.
# You need to check if they are integers.
# If they are not, it must return None.
# If they are all 3 integers, return the power between them.

def super_power(a, b, c):
    if (type(a) != int OR type(b) != int or type(c) != int):
        return None
    else: 
        return a ** b ** c
        
        
# 4
# Design a function with 3 parameters and
# returns this parameters into a tuple

def totuplue(x, y, z):
    return (x, y, z)