# Void vs Return

# Return returns values etc

max_value = max([ 3, 6, 2, 9 ])
chunks = ".split() returns a list of strings separated by spaces".split()
list_length = len([ "a", "b", "c" ])

def is_even( number ):
    if number % 2 == 0:
        return True
    return False



# Void simply performs action

print( "I return nothing, I just print things to the console" )

[ 4, 7, 3, 2 ].sort()
[ 1, 2, 4, 5 ].insert( 2, 3 )

def is_even( number ):
    if number % 2 == 0:
        print("{:d} is even". format( number ))
    else:
        print("{:d} is odd".format( number ))