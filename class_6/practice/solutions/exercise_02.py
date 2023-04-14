# 1
# create a new class called vehicle with the __init__ function
# inside the init, create two attributes, km and color. 

class vehicle:
    
    def __init__(self):
        self.km = 10
        self.color = "black"
        
car = vehicle()
print ("car km: '%s' and color: '%s'"  % (car.km, car.color))
# 2
# change the class vehicle and pass the km and color by parameters
# in init function

class vehicle:
    
    def __init__(self, km, color):
        self.km = km
        self.color = color
        
# --> error car = vehicle() porque faltan los parametros km y color
car = vehicle(color="blue", km=500) # by name
car2 = vehicle (20, "red") # by position

print ("car km: '%s' and color: '%s'"  % (car.km, car.color))
print ("car2 km: '%s' and color: '%s'"  % (car2.km, car2.color))

# 3
# add a new function (behaviour) in vehicle called lights, with
# one parameter "turn" defaults True. store this parameter into an attribute

class vehicle:
    def __init__(self, km, color):
        self.km = km
        self.color = color
        self.mylights = False

    def lights(self, turn=True):
        if turn == self.mylights:
            return
        
        self.mylights = turn
        if turn:
            print ("Lights ON")
        else:
            print ("Lights OFF")

# 4
# create two objects type vehicle and play with parameters and
# turn on or off the lights
car = vehicle(color="blue", km=500) # by name
car2 = vehicle (20, "red") # by position

car.lights()
car.lights(False)
car2.lights(False)
car2.lights(True)



