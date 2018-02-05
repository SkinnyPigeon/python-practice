# User range to generate a list of numbers

a = list( range( 0, 10 ))
# Range runs from the first number up to BUT NOT INCLUDING the last number
print(a)

print(a[0:5])
# Similarly slicing is up to BUT NOT INCLUDING the last number

print(a[2:len(a)])
print(a[2:])
print(a[:])

print(a[::2])
# This is called Step or Stepsized, super useful!!!!
print(a[0:6:2])
print(a[0:6:3])

print(a[-1])
print(a[-2])
# Careful with this, can cause bugs

print(a[2:-2])
# This is just weird, don't use

print(a[::-1])
print(a[::-2])
# This will run backwards through the list!!!!