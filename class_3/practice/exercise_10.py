#### practice with while, for, break, continue, else

# 1
# Print i as long as i is less than 10

i = 1

while i < 6:
  print(i)
  i += 1

# 2
# Stop the loop if i is 5

i = 1
while i < 10:
  if i == 5:
    break
  i+=1

# 3
# In the loop, when i is 5, jump directly to the next iteration
i = 1
while i < 6:
  i += 1
  if i == 3:
    continue

  print(i)

# 4
# Print a message once the condition is false.

i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")


# 5
# Loop through the items in the fruits list.

fruits = ["apple", "banana", "cherry"]
___ x __ fruits:
    print(x)

# 6
# In the loop, when the item value is "banana", jump directly to the next item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# 7
# Check de range function. what is it for?

r = range(10)
for x in r:
    print (x)

for y in range(0, 10, 2):
    print (y)

start = 5
stop = 20
step = 3

for x in range(start, stop, step):
    print (x)

