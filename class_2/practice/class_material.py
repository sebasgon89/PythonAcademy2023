#class material
##############################################################################################

# 01 - first program!

print ("first program!")

##############################################################################################

# 02 - PRINT TO SCREEN

#two  lines!
print("line 1")
print("line 2")

#error line
print("\")

#so, how print '\' ?
print("\\")


#The backslash (\) has a very special meaning when used inside strings - this is called the escape character.
#The word escape should be understood specifically - it means that the series of characters in the string escapes for the moment (a very short moment) to introduce a special inclusion.
#In other words, the backslash doesn't mean anything in itself, but is only a kind of announcement, that the next character after the backslash has a different meaning too.
#The letter n placed after the backslash comes from the word newline.

print ("line 1\n line 2")

#Single Quote
print ('It\'s alright.')
print ("It's alright.")

#Backslash
print("This will insert one \\ (backslash).")

#New Line
print("line\n and new line")

#Carriage Return
print("Hello\rkyndryls!")

#Tab
print("hello\thola\tciao")

#Backspace
print("hello \bbackespace")

#Octal value
print("\110\145\154\154\157")

#Hex value
print("\x48\x65\x6c\x6c\x6f")

##############################################################################################

# 03 - Type of data

x = 5
y = "John"
print(x)
print(y)

# what happends if use the same variable?

x = 5
x = "John"
print(x)

# strings! 
a = "Hello"
b = "hello" 
c = """
multi line string!
its great!
"""

# numbers! 
x = 1    # int
y = 2.8  # float
z = 1j   # complex


# bools 

x = True
y = False
print (x)
print (y)


#None

x = None
print (x)


##############################################################################################

# 04 - Operators

x = 5
y = 3

# Arithmetic Operators

print(x + y)
print(x - y) 
print(x * y) 
print(x / y) 
print(x % y) 
print(x ** y) 
print(x // y) 

# Assignment operators

x = 5
x += 3

print(x)

x = 5
x -= 3

print(x)

x = 5
x *= 3

print(x)

# Comparison Operators

x = 5
y = 10

print (x == y)
print (x != y)
print (x < y)
print (x > y)
print (x <= y)
print (x >= y)


# Logical, Identity & Membership

x = 5
print(x > 3 and x < 10)
print(x < 3 or x < 10)
print(not(x > 3 and x < 10))

x = 5
y = 2
z = 5

print (x is y)
print (x is z)

x = "hello"
print ("h" in x)
print ("a" not in x)


##############################################################################################

# 05 - Complex data types

fruitlist = ["apple", "banana", "cherry"]
print(fruitlist)
print (type(fruitlist))

fruittuple = ("apple", "banana", "cherry")
print(fruittuple)
print (type(fruittuple))

thisset = {"apple", "banana", "cherry"}
print (type(fruittuple))

mydict = {
  "name": "Anna",
  "middlename": "Linda",
  "surname": "Smith",
  "year": 1981
}
print(mydict)
print (type(mydict))

##############################################################################################

# 06 - Conditions & loops

a = 10
b = 200
c = 200

## if 

if b > a:
  print("b is greater than a")

if b < a:
  print("b is less than a")
else:
  print("b is greater than a")

if b < a:
  print("b is less than a")
elif b == c:
  print("b is equal c")
else:
  print("b is greater than a")

## while

i = 1
while i < 6:
  print(i)
  i += 1
  
  
fruitlist = ["apple", "banana", "cherry"]
i = 0
while i < len(fruitlist):
  print (fruitlist[i])
  i += 1

## for
for x in "banana":
  print(x)
  
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  

