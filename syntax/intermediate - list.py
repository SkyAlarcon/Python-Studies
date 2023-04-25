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