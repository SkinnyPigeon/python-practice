# import the pprint function from the pprint module as a function called pretty_print
from pprint import pprint as pretty_print

# imports the copy and deepcopy functions from the copy module
from copy import copy, deepcopy

nums_2d = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22]
]

print( nums_2d[1][3] )

print( nums_2d )
pretty_print( nums_2d )

nums_2d[2][1] = -5
pretty_print( nums_2d )

letters = [ "A", "B", "C", "D", "E" ]
letters_2d = [ letters, letters, letters ]
pretty_print( letters_2d )

letters_2d[0][0] = "F"
pretty_print( letters_2d )
# This changes all of the first letters to 'F' since they are references to the original array ( similar to Java )

letters = [ "A", "B", "C", "D", "E" ]
letters_2d = [ copy( letters ), copy( letters ), copy( letters )]
# Creates unique copies of the array

letters_2d[0][0] = "F"
pretty_print( letters_2d )

