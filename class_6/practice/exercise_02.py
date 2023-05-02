# 1
# create a new class called vehicle with the __init__ function
# inside the init, create two attributes, km and color.



# 2
# change the class vehicle and pass the km and color by parameters
# in init function



# 3
# add a new function (behaviour) in vehicle called lights, with
# one parameter "turn" defaults True.

class Vehicle():
    
    def __init__(self, km, color):
        self.km = km
        self.color = color
        self.lights = True

    def turn():
        self.lights = not(self.lights)

# 4
# create two objects type vehicle and play with parameters and
# turn on or off the lights

ferrari = Vehicle(100, "red")
jaguar = Vehicle(25, "Green")

print("Ferrari lights: % s" % ferrari.lights)
jaguar.turn
print("Jaguar lights: % s" % jaguar.lights)

