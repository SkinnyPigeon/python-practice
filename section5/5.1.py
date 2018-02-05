s = "hello world"
a = [ 4, 6, 9 ]

print( 5 in a )
print( 4 in a )
print( "ello" in s )
# in is a conditional check

for even_number in [ 2, 4, 6, 8, 10 ]:
    print( even_number )
    # add more code here..

odds = [ 1,3,5,7,9,11 ]
for odd_number in odds:
    print( odd_number )

print( range( len( odds )))

for index in range( len( odds )):
    print( "Index: {:d}, odd number: {:d}".format( index, odds[index]))