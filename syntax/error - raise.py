def checkInt (a):
    '''
    int -> void
    '''
    if not type(a) is int:
        raise TypeError ("Only integers allowed")
    if a < 0:
        raise Exception ("Only numbers above zero")
    
checkInt(10)
#checkInt(10.5)
#checkInt(-10)
# ^ test 'raise' by removing the comment

# RAISE
# Structure:
# raise [error/exception] ([message])
# 
# Another way of declaring exceptions and errors
# It WILL exit the code (at least it worked like this
# when I tested)