# METHODS
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in car.keys():
    print(f'key = {key}, value = {car[key]}')
# keys()
# Structure:
# dict.keys() - Returns a 'list' of all the keys on that dict #

for info in car.values():
    print(f'Info: {info}')
# values()
# Structure:
# dict.values() - Returns a 'list' of all values on that dict #

# We can use 'if' as well to check for keys and values: #
if "color" in car:
    print(car["color"])
else:
    print("No color")

if "Mustang" in car.values():
    print("Mustang is there")
else: print("No tang")
