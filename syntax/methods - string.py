# upper()
# Structure:
# string.upper() - returns the string, but all characters are upper case # 

string = "This is all upper-case"
stringUpper = string.upper()
print(stringUpper)

# isupper()
# Structure:
# string.isupper() - returns true or false either if the string is all upper-case or not respectively #

isUpper = string.isupper()
print(isUpper)
isUpper = stringUpper.isupper()
print(isUpper)


# lower()
# Structure:
# string.lower() - returns the string, but all characters are lower case # 

string = "THIS IS ALL LOWER-case"
stringLower = string.lower()
print(stringLower)

# isupper()
# Structure:
# string.isupper() - returns true or false either if the string is all upper-case or not respectively #

isLower = string.islower()
print(isLower)
isLower = stringLower[0].islower()
print(isLower)
print("------------------------------------------")


# isalpha()
# Structure:
# string.isalpha() - Returns boolean either if the string has only letters or not #

print("\nAlpha")
text = "abcdef"
alpha = text.isalpha()
print(alpha)
text = "abc def"
alpha = text.isalpha()
print(alpha)
text = "abcdef11"
alpha = text.isalpha()
print(alpha)
text = "abcdef...."
alpha = text.isalpha()
print(alpha)


# isdecimal()
# Structure:
# string.isdecimal() - Returns boolean either if the string has only numbers or not #

print("\nDecimal")
text = "123"
decimal = text.isdecimal()
print(decimal)
text = "123 123"
decimal = text.isdecimal()
print(decimal)
text = "123ased"
decimal = text.isdecimal()
print(decimal)
text = "123...."
decimal = text.isdecimal()
print(decimal)


# isalnum()
# Structure:
# string.isalnum() - Returns boolean either if the string has only letters AND numbers or not #

print("\nalnum")
text = "123"
alnum = text.isalnum()
print(alnum)
text = "123 123"
alnum = text.isalnum()
print(alnum)
text = "123ased"
alnum = text.isalnum()
print(alnum)
text = "123...."
alnum = text.isalnum()
print(alnum)


# isspace()
# Structure:
# string.isspace() - Returns boolean either if the string is only spaces AND line breaks or not #

print("\nSpace")
text = "123"
space = text.isspace()
print(space)
text = "123 123"
space = text.isspace()
print(space)
text = "123ased"
space = text.isspace()
print(space)
text = "123...."
space = text.isspace()
print(space)
text = "  \n\n\n\n"
space = text.isspace()
print(space)


# startswith()
# Structure:
# string.startswith(string) - Returns boolean either of the string starts EXACTLY (case sensitive) the as the parameter #

text = "Hello world!"
boolean = text.startswith("Hello")
print(boolean)
boolean = text.startswith("hello")
print(boolean)


# endswith()
# Structure:
# string.endswith(string) - Returns boolean either of the string ends EXACTLY (case sensitive) the as the parameter #

text = "Hello world!"
boolean = text.endswith("world!")
print(boolean)
boolean = text.endswith("World!")
print(boolean)


# join()
# Structure:
# string.join(list) - Returns a string with all the list itens concatenated and separated by the string given #

string = ", "
lst = ["cat", "dog", "bird", "giraffe", "kiwi"]
joined = string.join(lst)
print(joined)


# split()
# Structure:
# string.split(string2) - Returns a list with all words separated. The string2 is the condition to separate each word. If it is not informed, it will separate in each space or \n

text = "cat dog bird giraffe kiwi"
lst = text.split()
print(lst)
print()
text = '''cat
dog
bird
giraffe
kiwi'''
lst = text.split()
print(lst)
text = "catABCdogABCbirdABCgiraffeABCkiwi"
lst= text.split("ABC")
print(lst)


# strip()
# Structure:
# string.strip() - Returns a string with any spaces or \n removed from the start and end of the string #

text = "   \n\n\n   Sky do Céu    \n\n\n    "
newText = text.strip()
print(newText)
print('---------------')

# lstrip()
# Structure:
# string.lstrip() - Returns a string with any spaces or \n removed from the start of the string #

newText = text.lstrip()
print(newText)
print('---------------')

# rstrip()
# Structure:
# string.rstrip() - Returns a string with any spaces or \n removed from the end of the string #

newText = text.rstrip()
print(newText)
print('---------------')


