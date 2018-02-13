alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt( string, shift = 3 ):
    excrypted_string = ""
    for char in string:
        index = alpha.index( char )
        shifted_index = ( index + shift ) % len( alpha )
        excrypted_string += alpha[ shifted_index ]
    return excrypted_string

def decrypt( encrypted_string, shift = 3 ):
    decrypted_string = ""
    for char in encrypted_string:
        index = alpha.index( char )
        shifted_index = ( index - shift ) % len( alpha )
        decrypted_string += alpha[ shifted_index ]
    return decrypted_string

print( encrypt( "helloworld", 5 ))
print( decrypt( "mjqqtbtwqi", 5 ))
print( decrypt( encrypt( "abc" )))