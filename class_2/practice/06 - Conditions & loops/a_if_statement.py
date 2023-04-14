# IF! 

a = 10
b = 200
c = 200

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
elif a == c:
  print("a is equal c")
else:
  print("b is greater than a")

if a > b: print("a is greater than b")

print("A is greater") if a > b else print("B is greater")
