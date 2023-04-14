# open the IDLE
# play with time an dates!


# 1
# Get Current Date and Time
import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

# 2
# Get Current Date
date_object = datetime.date.today()
print(date_object)

# 3
# Date object to represent a date
d = datetime.date(2022, 11, 29) #yyyy, mm, dd
print(d)
d = datetime.date(2022, 10, 14) #yyyy, mm, dd
print(d)


# 4
# Get date from a timestamp
timestamp = datetime.date.fromtimestamp(1326244364)
print("Date =", timestamp)

# 5
# Print today's year, month and day
from datetime import date

# 6
# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# 7
# Time object to represent time
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

# 8
# Difference between two dates and times
from datetime import datetime, date

t1 = date(year = 2022, month = 7, day = 12)
t2 = date(year = 2021, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2022, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))

# 9
# Difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)

# 10
# Format date using strftime()
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)


