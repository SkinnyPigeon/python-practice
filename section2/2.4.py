n = 11
f = 1.2345678
s = "computer"

print("My number is {:d}".format(n))
print("My number is {:b}".format(n))

# There are many format types such as:
# e - exponents
# b - binary (base 2)
# o - octal (base 8)
# d - decimal (base 10)
# x - hexadecimal (base 16)
# f - floats (decimal number)
# s - strings (default if non is specified)

print("{:f}".format(f)) 
print("{:.3f}".format(f))
print("{:11.3f}".format(f))
print("{:011.3f}".format(f))

print("{0} {1} {2}").format(n,f,s)

print("{name} own(s) {amount} of {object}".format(
    name = "Euan",
    amount = 5, 
    object = "mangos"
))


