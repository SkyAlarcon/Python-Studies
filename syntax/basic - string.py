# STRINGS
# Concatenate
# Structure:
name = "Sky"
surname = "do Céu"
fullName = name + surname
print(fullName)

# To use special character, use an 'escape character' which is \ 
# The 'escape character' will not be printed, but will be interpreted #
text = 'That is Alice\'s cat'
print(text)

text = 'Sky\nis\nstudying\na\nlot'
print(text)

# Full table of 'escape character' and what will be printed
# \' = ' 
# \" = "
# \\ = \
# \t = tab 
# \n = new line

# Raw string
# Structure:
# r'string'
# Will print EVERYTHING, even the 'escape character'
# Just put an 'r' BEFORE the start of the string: 
print(r'Sky\nIs\nStudying')

# Multi lines strings
# Structure:
# '''
# String
# ''' #

text = '''This will be in
another line
and this too'''
print(text)

# To access specific parts, just use the same syntx as lists: #
text = " abcdefghijklmnop"
print(text[2])
print(text[2:5])
print(text[5:12])
print(text[:4])
print(text[14:])
# Each character ocupies an index of the string #

text = 'Hello world!'
print("Hello" in text)
print("hello" in text)

# Strings takes into consideration upper and lower case #

# String interpolation
# Structure:
# 'string %s more-string %s even-more-string' % (variable1, variable2) #

name = "Sky"
age = 24
print("Hello %s! You said you are %s y.o., is this correct?" %(name, age))

# Format strings 
# Structure: 
# f'string {variable} more-string {variable2} even-more-string {variable3}' 
# Note: You can make calculation inside the brackets #
print(f'Hello {name}! You said you are {age+1} y.o., is this correct?')
