#!/usr/local/bin/python3.6

my_list = [ 1, 2, 3, 4, 5 ]
my_tuple = ( 2, 7, 8, 9, 10 )
my_string = "Hello World!"

print( "List: ", dir( my_list ))
print( "Tuple: ", dir( my_tuple ))
print( "String: ", dir( my_string ))
# Holy shit!!!!! Check out DIR. What a function!!!!!

print( '__iter__' in dir( my_list ))
print( '__iter__' in dir( my_tuple ))
print( '__iter__' in dir( my_string ))

for elem in my_list:
    print( elem )
# Since the list has the property __iter__ it can be looped in this way


list_iterator = iter( my_list )
while True:
    try:
        next_elem = next( list_iterator )
        print( next_elem )
    except StopIteration:
        break
# This is what the for loop is doing including a very nice StopIteration exception - very nice

