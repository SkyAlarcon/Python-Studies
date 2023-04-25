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

