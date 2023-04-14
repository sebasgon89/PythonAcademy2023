x = 8
y = 3
l = ["red", "blue", "black"]

#1
# multiply x and y and print the result

print(x*y)

#2
# Divide x and y and print the result

print(x/y)

#3
# how check the color "blue" in the list "l"

print("blue in the list?", "blue" in l)

#4
# show the second element in list "l"

print("second element:", l[1])

#5
# Change the value from "black" to "white", in the list "l".

print ("prev", l)
l[2] = "white"
print ("after change", l)


#6
# add the color yellow to the list l (if not remember the function, show the options with dir)

l.append("yellow")

#7
# Insert the color brown in the 2 position on the list "l"

l.insert(1, "brown")

#8
# remove the color "blue"

l.remove("blue")

#9
# How show the last element in "l"?

l[-1]

# 10
# how print a range elements in the list "l" ?



# 11
# Create a new tuple called "t" with the content of list "l"

t = tuple(l)

# 12
# show how many elements in tuple "t"

len(t)

# 13
# Use negative index to show the last element in tuple "t"

t[-1]
