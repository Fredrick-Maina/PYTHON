"""
Consider the following example function definitions paying close attention to the markers / and *:

"""

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


"""
The first function definition, standard_arg, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:
"""
print(standard_arg(2))

print(standard_arg(arg=2))

"""
The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function definition:

"""

print(pos_only_arg(1))

# Uncomment one after the other to observe the different types of errors that arise

# print(pos_only_arg(arg=1)) 


"""
The third function kwd_only_arg only allows keyword arguments as indicated by a * in the function definition:

"""
# print(kwd_only_arg(3))
print(kwd_only_arg(arg=3))

"""

And the last uses all three calling conventions in the same function definition:

"""
# print(combined_example(1, 2, 3))
print(combined_example(1, 2, kwd_only=3))


print(combined_example(1, standard=2, kwd_only=3))


# print(combined_example(pos_only=1, standard=2, kwd_only=3))
