import datetime as dt

def add( a, b, c ):
    return a + b + c

print( add( 1,2,3 ))
print( add( "A","B","C" ))

def add( *numbers ):
    # Ace. Unlimited parameters
    total = 0
    for n in numbers:
        total += n
    return total

print( add( 1, 2, 3, 4, 5, 6 ))

def record_time( message, time = dt.datetime.now() ):
    # This is called a default parameter
    # save to file for instance
    print( "{:}, time: {:}".format( message, time ))

record_time( "It is the evening" )
record_time( "It is the evening", "February 13th 2018" )
# Can overwrite default parameters

