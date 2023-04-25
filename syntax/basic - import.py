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