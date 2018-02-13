# Doubles the number n
# double(2) -> 4
# double(15) -> 30

def double(n):                      # double(3)       +2 
                                    #           ⬇️ 
    # base case                     # double(2)       +2
    if n == 0:                      #           ⬇️ 
        return 0                    # double(1)       +2
                                    #           ⬇️ 
    # recursive call                # double(0)        0  
    return double( n - 1 ) + 2      #                 ⬆️
                                    #((((0) + 2) + 2) + 2) = 6

def exponentiate( b, e ):

    # Base case
    if ( e == 0 ):
        return 1

    # Recursive call
    return exponentiate( b, e - 1 ) * b

    # See video for diagram as jeez