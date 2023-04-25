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

listToOperate = ["a", "b", "c", "d", "e", "f", "g"]
# LIST OPERATORS/FUNCTIONS
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

# Concat and multiply
listToSum = ["a", "b", "c"]
listToSum2 = ['d', 'e', 'f']
# To concatanate two or more lists, just use '+'
listaSum = listToSum + listToSum2
print(listToSum)
# To multiply a list, use '*'
listaMult = listaSum * 2
print(listaMult)