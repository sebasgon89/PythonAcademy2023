# 1
# create a new class called Person. Define into init this attributes:
#   age ,name, surname, date of birth and ID
# define a default for this attributes and include them in init

class Person:
    def __init__(age=33, name="Seba", surname="Goetz", date_of_birth="1989-07-03", ID="1234"):
        self.name = name
        self.surname = surname
        self.age = age
        self.date_of_birth = date_of_birth
        self.ID = ID


# 2
# check with dir and help, the __eq__ function

# 3
# create two objects of type Person.
# Check what happens if you compare them with the operator ==

# 4
# override the eq function, so python returns True if the ID is the same

# 5
# now, check with two objects like step 3
