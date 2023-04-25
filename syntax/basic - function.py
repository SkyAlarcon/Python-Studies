def firstFunc ():
    '''
    () -> void
    '''
    print("This is a function")
    return

# FUNCTIONS
# Structure:
# def [function name] ([function parameters]) :
#   '''
#   ([parameters]) -> [type of what is returned]
#   ''' 
#   --identation
# 
# To call a function, just use [function name]([parameters])
# 
# Due to scopes, variables created INSIDE the function lines
# WILL NOT be accessible on a global scale EXCEPT if you 
# use:

def secondFunction ():
    '''
    () -> void
    '''
    global globalVariable
#   ^ must use this syntax to create the variable OUTSIDE the function scope
#   and access it globally
    globalVariable = 1
    return

secondFunction()
print(globalVariable)

# It's also possible to make parameters already have an value like this:
def thirdFunction (str = "placeholder"):
    '''
    (str) -> void
    '''
    print(str)
    return
thirdFunction()
thirdFunction("text")