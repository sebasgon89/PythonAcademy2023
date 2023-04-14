#1
# What is the meaning of the "len" function?

k = "hola"
l = [1, 2, 3]
print ("len k", len(k))
print ("len l", len(l))

#2
# show the first character of the string k
print ("first character of 'k'", k[0])

#3
# show the charracters "ol" from string k
print (k[1:3])

#4
# What is the meaning of the "strip" function?

a = " Kyndryls Goals "
print (a.strip())

#5
# List all functions included in string type

dir(a)

#6
# List help for the function strip

help(a.strip)

#7
# Show the content of var "a" in UPPERCASE (tip use the point 5 and 6)

a.upper()

#8
# Show the content of var "a" in lower case (tip use the point 5 and 6) 

a.lower()
# 9
# Replace "K" with "P" in var "a"(tip use the point 5 and 6)

a.replace("K", "P")

