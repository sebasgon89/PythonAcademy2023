# 1
# use the class person from previous excercise.

class Person:
    def __init__(self, age=20, name="Leo", surname="Messi", birth="1985-01-01", ID=12345):
        self.age = age
        self.name = name
        self.surname = surname
        self.birth = birth
        self.ID = ID

# 2
# create a class called Student
# that will inherit properties and methods from a class named Person

class Student(Person):
    def __init__(self):
        Super.__init__()

# 3
# Create a function called "current" in the student class, which receives as a
# parameter the course to which the student is assigned.

def current(course):
    self.course = current

# 4
# What happens if we want to show the course in an object that never
# executes the "current" function?

# 5
# fix the previous problem (hint: use the init! but on Student class ... )

