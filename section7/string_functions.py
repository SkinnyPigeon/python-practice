def first_half(s):
    return s[:len(s)/2]

def last_half(s):
    return s[len(s)/2:]

# We are currently running THIS script
# Since we don't want to run these tests everytime this is imported we can use this if statement to run the tests as we are building it and it won't get called by exxternal sources. Pretty nifty although will get very messy.
if __name__ == '__main__':
    print( "Testing string functions" )
    assert first_half( "abcd" ) == "ab", "First half is failing"
    assert last_half( "abcd" ) == "cd", "First half is failing"
