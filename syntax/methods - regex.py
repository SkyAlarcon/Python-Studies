import re

# compile()
# Sturcture:
# re.compile(string) - returns a regex object compiled
# \d - digits 0 to 9
# Search for regex cheat sheet 
# https://www.dataquest.io/blog/regex-cheatsheet/ or 
# https://pynative.com/python-regex-special-sequences-and-character-classes/
# If you'll use MORE than one time the same type of
# character, you can use:
# \d{number} - number is how many time the specified character
# will be repeated #

telNumber = re.compile(r"\d{5}-\d{4}")
print(telNumber)

text = "My phone number is: 00000-0000. Call me ASAP!"

# serch()
# Structure:
# regexObject.search(string/or any piece of data, I actually didn't understood it properly) - Returns a re.Match object #

result = telNumber.search(text)

print(result.group())