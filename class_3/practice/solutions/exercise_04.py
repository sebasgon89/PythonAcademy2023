#1
#how print the type of var a?
a = "hello"
print(type(a))
a = 10
print(type(a))
a = "hello"
print(type(a))

#2
#Change the following lines to show float instead of integer
x = 31
print(type(x))

# case A
x = 31.0
print(type(x))
#case B
x = float(31)
print(type(x))
#case C
x = 31
print(type(float(x)))


#3
# How compare if the type for var x and a is the same?
type(a) == type(x)

#4
# Define the content of l to show "list" on the print

# option A
l = []
print (type(l))
# option B
l = list()
print (type(l))
# option C
l = [1, 2, 3]
print (type(l))


# 5
# Define a tuple with the contents of the variables x, a and l and print the type

t = (x, a, l)
print (type(t), t)

#6
#Create a dictionary with the following keys: "name", "surname", "age", "project" and complete the information with your data

d = {
    "name": "alfonso",
    "surname": "palomares",
    "age": 41,
    "project": ["p1", "p2", "p3"]
    }

