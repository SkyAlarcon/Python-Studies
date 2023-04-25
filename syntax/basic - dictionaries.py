car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car["brand"])
print(car.get("year"))

# DICTIONARIES
# Structure:
# variable = {
#               "key1": value,
#               "key2": value,
#               "key3": value"             
#            }
# To access values:
# variable["key"] or variable.get("key", "Custom msg")
# If the key DOESN'T exists, the first method will CRASH
# The second, on the other hand, will return 'None' or a custom msg #

# Add a new key: value
car["color"] = "red"
print(car["color"])

# Deleting
del car["new"]
print(car)