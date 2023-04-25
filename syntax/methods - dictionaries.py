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
# or using the update()
car.update({"new": True})
print(car["new"])
car.update({"new": False})
print(car["new"])
# or use pop() to return the removed value
cor = car.pop("color")
print(car)
print(cor)

# or use popitem()
ano = car.popitem()
print(car)
print(ano) # return a tuple with the key and value removed
# to remove EVERYTHING use clear()
car2 = {"brand": "Ford", "model": "Mustang", "year": 1964}
car2.clear()
print(car2)
print()

# To copy a dict, you MUST use copy()
person = {"name": "Sky", "tag": "doCéu", "age": 24, "working": True}
personNotCopy = person
personCopy = person.copy()
# otherwise it will reference the existing list and
# any changes in it will change the "copy" too
del person["working"]
print(person)
print(personNotCopy)
print(personCopy)

# To make default statements so you can check and add "key: values" if necessary
person.setdefault("alive", True)
print(person)
# If it doesn't exists, it will create and set the value
# if it exists, nothing changes


# To group dicts you use:
person = {"name": "Sky", "tag": "doCéu", "age": 24, "working": True}
sensitiveInfo = {"CPF": 00000000000, "RG": 000000000, "savings": 0}
person_plus_sensitiveInfo = {**person, **sensitiveInfo}
print(person_plus_sensitiveInfo)