#1
#Create a variable named projectname and assign the value MICROSOFT to it.

projectname = "MICROSOFT"

#2
#Create a variable named k and assign the value 41 to it.

k = 41

#3
#Display the sum of 41 + 12, using two variables: k and y (dont change the var content!)

y = 12
print ( "result sum:", 41 + 12)
print ( "result sum with vars:", k + y)

#4
#Create a new var called z and assign k + y. and display  the result.

z = k + y
z=k+y # son equivalentes con el anterior
print ("new var 'z'", z)

#5
#Remove the ilegal characters on the var name
## --->> 5the-last_name = "Gonzalez"
#correct sentence
the_last_name = "Gonzalez"

#6
#define the correct syntax to assing the same value to all vars (a, b and c)

a = b = c = "kyndryl"
print ("a:", a, "b:", b, "c:", c)

#7
# complete the correct syntax to assing two different elements in two vars
var1, var2 = "info1", "info2"

#8
# how to display 23 times "HOLA!" without writing it 23 times

h = "HOLA!"
print ("repito string: ", h * 23)


#9 
# display all vars used using only one print function, separated by TAB and close the line with 2 returns

print (projectname, k, y, z, the_last_name, a, b, c, var1, var2, h, sep="\t", end="\n\n")

# 10
# save this file and execute all exercises


