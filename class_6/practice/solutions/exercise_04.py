# 1
# use the class person from previous excercise.

class Person:
    def __init__(self, age=20, name="Leo", surname="Messi", birth="1985-01-01", ID=12345):
        self.age = age
        self.name = name
        self.surname = surname
        self.birth = birth
        self.ID = ID

    def compare(self, value):
        if type(value) != type(self):
            return False
        
        return self.ID == value.ID 

    def __eq__(self, value):
        return self.compare(value)
    
# 2
# create a class called Student
# that will inherit properties and methods from a class named Person

class Student(Person):
    pass

ana = Student(name="Ana")
ana2 = Student(name="Ana")
print ("son iguales %s" % (ana == ana2))
# 3
# Create a function called "current" in the student class, which receives as a
# parameter the course to which the student is assigned.

class Student(Person):
    def current(self, course="python"):
        self.course = course

ana = Student(name="Ana")

# 4
# What happens if we want to show the course in an object that never
# executes the "current" function?

## --> ERROR print ("el curso de ana es %s" % ana.course)
## if we not call the function current previusly

# 5
# fix the previous problem (hint: use the init! but on Student class ... )

class Student(Person):

    def __init__(self, age=20, name="Leo", surname="Messi", birth="1985-01-01", ID=12345,course=None):
        super().__init__(age, name, surname, birth, ID)
        self.course = course
        
    def current(self, course="python"):
        self.course = course

ana = Student(name="Ana")
print ("el curso de ana es %s" % ana.course)
    
