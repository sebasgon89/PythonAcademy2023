# 1
# create a new class called Person. Define into init this attributes:
#   age ,name, surname, date of birth and ID
# define a default for this attributes and include them in init

class Person:
    def __init__(self, age=20, name="Leo", surname="Messi", birth="1985-01-01", ID=12345):
        self.age = age
        self.name = name
        self.surname = surname
        self.birth = birth
        self.ID = ID


juan = Person(30, "juan", "gomez", "1992-01-01", ID=123)
juan2 =  Person(30, "juan", "gomez", "1992-01-01", ID=123)
print ("juan y juan2 son iguales? '%s'" % (juan == juan2))

# 2
# check with dir and help, the __eq__ function

# help(juan.__eq__) 
# 3
# create two objects of type Person with the same attributes, and
# Check what happens if you compare them with the operator ==

juan = Person(30, "juan", "gomez", "1992-01-01", ID=123)
juan2 =  Person(30, "juan", "gomez", "1992-01-01", ID=123) 
print ("#3 ---> juan y juan2 son iguales? '%s'" % (juan == juan2))

# 4
# override the eq function, so python returns True if the ID is the same

class Person:
    def __init__(self, age=20, name="Leo", surname="Messi", birth="1985-01-01", ID=12345):
        self.age = age
        self.name = name
        self.surname = surname
        self.birth = birth
        self.ID = ID

    def compare(self, value):
        if type(value) != type(self):
            print ("type %s -- type %s" % (type(value), type(self)))
            return False
        
        return self.ID == value.ID 

    def __eq__(self, value):
        return self.compare(value)


# 5
# now, check with two objects like step 3

juan = Person(30, "juan", "gomez", "1992-01-01", ID=123)
juan2 =  Person(30, "juan", "gomez", "1992-01-01", ID=123) 
print ("#4 ---> juan y juan2 son iguales? '%s'" % (juan == juan2))

