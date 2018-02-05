n = int( input( "n = "))

divisors = []

# for n in range( -10, 10 ):

if n >= 2:
    for divisor in range( 2, n ):
        if n % divisor == 0:
            divisors.append( divisor )

    if len( divisors ) == 0: #prime!
        print( "{:d} is prime!".format(n))
    else:
        print( "{:d} is not prime because {:} divide {:}".format( n, str( divisors ), n )) 
else:
    print( "{:d} is not prime".format(n))

# 728293 is a prime!