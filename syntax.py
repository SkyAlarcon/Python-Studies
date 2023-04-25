# To run on the integrated terminal:
# - Open the folder of the file
# - write "py [file].py" #

str(3)
int("4")
float("4.01")

# Converting variables
# Pretty self-explanatory:
# str() = string
# int() = integer
# float() = real numbers #
print("------------------------------------------")

true = True
false = False
# Booleans are written with uppercase #

# < <= == >= >
# Logical comparators
# Most works only with numbers,
# except '==' which means 'equals to' 
# so it can be aplied to strings and lists (probably dicts too)

# Logical expressions
# You can use 'and', 'or' and 'not'
# which is self-explanatory #

print(5 < 3)
# This returns a BOOLEAN
print("------------------------------------------")

if 5 > 3 :
    print("Hello world")
else :
    print("GG world")

if 5 < 3 :
    print("GLHF")
elif (5 > 3) :
    print("IZI")
else :
    print("Last interaction")

# IF ELSE ELIF 
# Structure:
# if [condition]: --can be used ()
#   --identation
# else:
#   ---identation
# _______________________________________
# If you are doing only ONE command,
# you can put it on the SAME LANE
print("------------------------------------------")

index = 0
while index < 5:
    index += 1
    if (index == 3): continue
    print(index)

# WHILE
# Structure 
# while [condition]:
#   --identation
# _______________________________________
# Remember to update any variables you
# are using at the verification of the
# while to see if it should repeat itself

# CONTINUE & BREAK
# continue: skips to the next iteration of the loop
# break: stops and skips any iteration left of the loop
print("------------------------------------------")

for i in range(5):
    print ("Count:" + str(i))
    if i == 4: break

# FOR
# Structure:
# 
# for [variable] in range([number]):
#           ^ variable starts at 0 and goes up one by one
#                   until number
#   --iteration 
# 
# for [var] in range ([number1], [number2]):
#                       ^           ^ finish number 
#                       start number 
# 
# for [var] in range ([number1], [number 2], [number3]):
#                       ^           ^           ^ how much will be added
#                      start       finish #       (or subtracted) after iteration
print("------------------------------------------")

import random
print("Random integer:", random.randint(1,10))

# Importing libraries
# Structure:
# import [library]
# 
# To access it you must use: [library].[function]
# You need to use the library as a prefix!

from sys import exit
#               ^ to import ALL function, use '*' instead
print("Write 'exit' to stop the program:")
var = input()
if (var == "exit"): 
    print("Exiting")
    exit()

# Another structure:
# from [library] import *
#                       ^ this imports all functions with their
#                           respective name
# 
# To access a function of the library you use: [function]
print("------------------------------------------")

def firstFunc ():
    '''
    () -> void
    '''
    print("This is a function")
    return

# FUNCTIONS
# Structure:
# def [function name] ([function parameters]) :
#   '''
#   ([parameters]) -> [type of what is returned]
#   ''' 
#   --identation
# 
# To call a function, just use [function name]([parameters])
# 
# Due to scopes, variables created INSIDE the function lines
# WILL NOT be accessible on a global scale EXCEPT if you 
# use:

def secondFunction ():
    '''
    () -> void
    '''
    global globalVariable
#   ^ must use this syntax to create the variable OUTSIDE the function scope
#   and access it globally
    globalVariable = 1
    return

secondFunction()
print(globalVariable)

# It's also possible to make parameters already have an value like this:
def thirdFunction (str = "placeholder"):
    '''
    (str) -> void
    '''
    print(str)
    return
thirdFunction()
thirdFunction("text")
print("------------------------------------------")

def division(a, b):
    '''
    (int, int) -> int
    '''
    try:
        return a/b
    except ZeroDivisionError:
        print ("Error: Cannot divide by zero")
    except TypeError:
        print ("Error: Cannot divide using strings")
    finally:
        print ("Finished")

print(1, division(1, 0))
print(2, division("a", 1))
print(3, division(4, 2))

# TRY & EXCEPT
# Structure:
# try:
#   --identation
# except [error type --not obligatory]:
#   --identation
# finally:
#   --identation
# 
# May have multiple exceptions

def checkInt (a):
    '''
    int -> void
    '''
    if not type(a) is int:
        raise TypeError ("Only integers allowed")
    if a < 0:
        raise Exception ("Only numbers above zero")
    
checkInt(10)
#checkInt(10.5)
#checkInt(-10)
# ^ test 'raise' by removing the comment

# RAISE
# Structure:
# raise [error/exception] ([message])
# 
# Another way of declaring exceptions and errors
# It WILL exit the code (at least it worked like this
# when I tested)

assertTest = "test"
#assert assertTest == "not test", "Should be a test"
# ^ test 'asserst' by removing comment

# ASSERT
# Structure:
# assert [logical expression], [custom message]
# It's used to make sure of the intended variable
print("------------------------------------------")

lista = [1, 2, "cat", "dog"]
lista2 = [4, 5, lista]
print (lista2)

# LISTS
# Structure:
# [name] = []
# Can have integers, strings, dicts, lists, basically anything
# To access, use:
# [name][index] such as:
print (lista2[2])
# and if you have a list inside another list:
print (lista2[2][0])
# You can also return a part of the list 
print(lista2[0:2])
#            ^ ^will finish BEFORE this index
#           will start AT this index
# If you don't set an start/finish index 
# it will start at 0 ou finish at the last index
# respectively
# Negative indexes are a thing and it will count backwards 
# lista[-1] will be the last position

print(len(lista2))
# LENGTH 
# List length, self-explanatory
# This WILL NOT count sub-lists!

# Concat and multiply
listToSum = ["a", "b", "c"]
listToSum2 = ['d', 'e', 'f']
# To concatanate two or more lists, just use '+'
listaSum = listToSum + listToSum2
print(listToSum)
# To multiply a list, use '*'
listaMult = listaSum * 2
print(listaMult)
print("------------------------------------------")

listToOperate = ["a", "b", "c", "d", "e", "f", "g"]
# LIST OPERATORS/FUNCIONS
# Delete/Remove item
# Structure:
# del [index] - Deletes the item of the given index #
del listToOperate[0]
print(listToOperate)

# Check/Verify item existence
# Structure:
# [what you want to check] in [list] #
exists = "d" in listToOperate
print(exists)

numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# MIN MAX SUM
# Structure:
# min([list]) 
# self-explanatory
toPrint = min(numbersList)
print(toPrint)
toPrint = max(numbersList)
print(toPrint)
toPrint = sum(numbersList)
print(toPrint)
print("------------------------------------------")

listMethods = ["Sky", "Re", "Cami", "Ju", "Del", "Lu"]
# LIST METHODS 
# Structure:
# list.index("string") - Returns the index of the parameter you gave 
# Errors WILL break the routine #
print("index")
listIndex = listMethods.index("Cami")
print(listIndex)

# Structure:
# list.append("string") - Inserts an item at the end of the list #
print("append")
listMethods.append("Ro")
print(listMethods)

# Structure:
# list.insert(index , "string") - Inserts an item at the the exact index of the list #
print("insert")
listMethods.insert(1, "Ju")
print(listMethods)
listMethods.insert(100, "Ju")
print(listMethods)
# If the index goes beyond the last index, the function you work similarly as the ".append()"

# Structure:
# list.pop([index]) - Remove and returns the last item of the list if no index is specified
# If you specify the index, will remove the said index #
print("pop")
popped = listMethods.pop()
listMethods.pop(2)
print(listMethods)
print("popped: " + popped)

# Structure:
# list.sort() - Self explanatory. Works with strings or numbers #
print("sort")
listMethods.sort()
print(listMethods)

# Structure:
# list.reverse() - Reverses the order of the list #
print("reverse")
listMethods.reverse()
print(listMethods)

# Structure:
# list.count(to-count) - counts the number of occurrences of something #
print("count Ju")
counter = listMethods.count('Ju')
print(counter)
print("------------------------------------------")


listDogs = ["Rex", "Totó", "Auau", "Mia", "Thor", "Candy"]
for index, dog in enumerate(listDogs):
    print("Index: " + str(index))
    print("Dog: " + dog)
    print()

# for in enumerate()
# When you call 'enumarate()' it will return two values
# index and the actual value of that said index of the list #
print("------------------------------------------")


dog = ["brown", 12, "Bulldog"]
color, age, breed = dog
print(color, age, breed)

# To assign multiple variables from the same list
# just use a comma to separate and assign the list
# YOU MUST use ALL the indexes, otherwise it will crash 
# It will assign by the written order, that means:
# First variable = first index and so on #
print("------------------------------------------")


tupleTest = ("apple")
print(type(tupleTest))
tupleTest = ("apple",)
print(type(tupleTest))
tupleTest = ("apple", 'pear', 'melon')
print(tupleTest[1])

# TUPLES
# Structure:
# [variable] = (item, item, item)
# If you have only ONE item, you MUST use a comma after it
# otherwise python won't recognize as a tuple
# Tuples can't change values like lists
# To access values is all the same as lists #
print("------------------------------------------")

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

print()
print()
print("Methods")
# METHODS

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

# Modifying the dict
print()
print()
print("Modifying the dict")

# Add a new key: value
car["color"] = "red"
print(car["color"])

# or using the update()
car.update({"new": True})
print(car["new"])
car.update({"new": False})
print(car["new"])

# Deleting
del car["new"]
print(car)

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