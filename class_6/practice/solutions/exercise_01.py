# 1
# complete the first sentence and create a class named PrimeraClase

class PrimeraClase:
    x = "hello"

# 2
# create an object called "primerObjeto", type "PrimeraClase"
# and print the x attribute

primerObjeto = PrimeraClase()
print ("muestro el atributo X del objecto '%s'" % primerObjeto.x)

# 3
# Assign a new atribute called "y" with value "bye" to object "primerObjeto"
# and print it

primerObjeto.y = "bye"
print ("muestro el atributo Y del objecto '%s'" % primerObjeto.y)



# 4
# Create a new object called "segundoObjeto" and check their attributes

segundoObjeto = PrimeraClase()
dir (segundoObjeto)

# 5
# compare types between objects.

print ("type 1er objeto", type (primerObjeto))
print ("type 2do objeto", type (segundoObjeto)
print ("¿Son iguales?", str(type (primerObjeto) == type (segundoObjeto))

