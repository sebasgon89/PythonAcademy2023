

class Example1(object):
    def __init__(self, val = 10):
        self.first = val
        self.__second = val * 2


example_object_1 = Example1()
example_object_2 = Example1(2)

#print (example_object_1.__dict__)
#print (example_object_2.__dict__)



class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass



class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass



class Vehicle:
    def info(self):
        print ("info vehicle")


class Car(Vehicle):
    def info(self):
        print ("info car")
        super().info()


class Truck(Vehicle):
    def info(self):
        print ("info Truck")
        super().info()



class Argentina():
    def capital(self):
        print("CABA is the capital of India.")
  
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
 
obj_arg = Argentina()
obj_usa = USA()
#for country in (obj_arg, obj_usa):
#    country.capital()
   

class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
#obj_bird.intro()
#obj_bird.flight()
 
#obj_spr.intro()
#obj_spr.flight()
 
#obj_ost.intro()
#obj_ost.flight()
