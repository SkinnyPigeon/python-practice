# More recursive functions

def count_vowels( string, i = 0 ):
    
    if( i == len( string )): return 0

    char = string[i]
    if char in 'aeiou':
        return count_vowels( string, i + 1 ) + 1
    return count_vowels( string, i + 1 ) + 0   # Don't need the plus 0 

print( count_vowels( "helloworld" ))
print( count_vowels( "hello" ))
print( count_vowels( "world" ))


# 345 -> 3+4+5 = 12
# 345
# 34
# 3
# 0

# 6789 -> 6+7+8+9 = 30

def digit_sum( number ):
    if number == 0: return 0
    return digit_sum( number // 10 ) + number % 10 

print( digit_sum( 345 ))
print( digit_sum( 6789 ))


# 0 1 2 3 4 5 6 .. ( index )
# 1 1 2 3 5 8 13 ...

def fib( number ):
    if number == 0 or number == 1: return 1
    return fib( number - 2 ) + fib( number - 1 )

for i in range(10):
    print( fib( i ))




