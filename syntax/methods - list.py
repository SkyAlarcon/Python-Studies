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