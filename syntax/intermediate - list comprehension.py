# Similar to numerical sets in math such as:
# { x | x^0.5 is a natural number and x < 100} 
# Which would translate, as a for, to: 

for x in range (1, 101):
    if (int(x**0.5) == x**0.5):
        print(x)


comprehension = [x for x in range(1,101) if int(x**0.5) == x**0.5]
print(comprehension)