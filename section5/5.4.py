alpha = 'abcdefghijklmnopqrstuvwxyzABCDWEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'aeiouAEIOU'
my_string = "I will not write what the teacher tells me to!"

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

total = 0
for n in numbers:
    if n % 2 == 0:
        total += n
    # print( total )
    # If print is here it will print it each time it gets here
print( total )
# If print is here it will only print at the end. Such a weird way to do syntax

characters = []
for char in my_string:
    if char not in vowels and char in alpha:
        characters.append( char )
consonants = "".join( characters )
print( consonants )



