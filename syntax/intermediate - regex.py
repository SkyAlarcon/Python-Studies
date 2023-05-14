import re
# Import of regular expressions library #

# Regular Expressions (a.k.a. Regex)
# It's used to create and look for specific data in your provided info such as a phone number #

telNumber = re.compile(r'\d\d\d\d\d-\d\d\d\d')
text = "My phone number is: 00000-0000. Call me ASAP!"
result = telNumber.search(text)
print("Phone found:" + result.group())