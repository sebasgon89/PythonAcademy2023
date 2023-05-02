# 1
# create a class Teacher,
# that will inherit properties and methods from a class named Person

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

class Student(Person):

    def __init__(self, age=20, name="Leo", surname="Messi", birth="1985-01-01", ID=12345,course=None):
        super().__init__(age, name, surname, birth, ID)
        self.course = course
        
    def current(self, course="python"):
        self.course = course

class Teacher(Person):
    pass

# 2
# create a class exam with two parameters, Student object and Teacher
# Check that the student and the teacher are not the same person.
# If so, throw an exception. (remember, raise Exception('your text...') )

class Exam():

    def __init__(self, student, teacher):
        if not isinstance(student, Student):
            raise Exception ("the first parameter is a student! not other stuff")

        if not isinstance(teacher, Teacher):
            raise Exception ("the sec parameter is a Teacher! not other stuff")

        if student.compare(teacher):
            raise Exception("Student and Teacher are the same")
        
        self.student = student
        self.teacher = teacher
        self.grade = None


# 3
# define a function that receives the test grade by parameter and store it
class Exam:
    def __init__(self, student, teacher):
        if not isinstance(student, Student):
            raise Exception ("the first parameter is a student! not other stuff")

        if not isinstance(teacher, Teacher):
            raise Exception ("the sec parameter is a Teacher! not other stuff")
        
        self.student = student
        self.teacher = teacher
        self.grade = None

    def test(self, grade=4):
        if isinstance(grade, int):
            self.grade = grade
        else:
            raise Exception("ojo el grade tiene que ser ENTERO")


