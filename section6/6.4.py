# => "123" -> "321"
# => "abcd" -> "dcba"
# => "11121" -> "12111"

def reverse( string ):
    new_string = ""
    for i in range( len( string )):
        new_string += string[ len( string ) - i - 1 ]
        # Sweet. Loop backwards!!!!
    return new_string

print( reverse( "123" ))
print( reverse( "abcd" ))
print( reverse( "11121" ))

# is_palindrome
# palindrome examples: "1", "121", "abba", "56765", "bbbbb", ""

def is_palindrome( string ):
    for i in range( len( string ) // 2 ):
        # need the double slash there
        if string[i] != string[ len( string ) - i - 1 ]:
            print( "No this is not a palindrome" )
            return 
    print( "Yes this is a palindrome" )

is_palindrome( "1" )
is_palindrome( "121" )
is_palindrome( "abba" )
is_palindrome( "123" )
is_palindrome( "hello" )

def is_palindrome( string ):
    if string == string[ ::-1 ]:
        print( "Yes this is a palindrome" )
    else:
        print( "No this is not a palindrome" )

is_palindrome( "1" )
is_palindrome( "121" )
is_palindrome( "abba" )
is_palindrome( "123" )
is_palindrome( "hello" )
# def is_palindrome( string ):
#     pass
# if we put the word "pass" in, it allows us to define a function without putting anything in it so it will complile. good for sketching out classes( assuming there are classes )