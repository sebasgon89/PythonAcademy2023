
car =	{
  "brand": "Nissan",
  "model": "Note",
  "year": 2019
}

car2 =	{
  "brand": "Nissan",
  "model": "kiks",
  "year": 2021,
  "color": "red"
}


# 1
# Use the method get to show the model

car.get("model")
car2.get("model")

# 2
# use the method get to show the "color" or "blue" (if color is not present) in bouth dicts

car.get("color", "blue")
car2.get("color", "blue")

# 3
# add or change the color in dict car to "black"
car["color"] = "black"

# 4
# remove element "year" from car2 dict (check the function pop with help)

car.pop("year")

