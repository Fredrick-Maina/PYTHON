"""
The first part evaluated to true and prints welcome,
because the or statement needs only one side to evaluate to true

name == "Jim" evaluates to False since "James" == "Jim" is false
"Fred" evaluates directly to True because it is a non-empty string
"""

name = "James"
if name == "Jim" or "Fred":
     print("Welcome")
else:
     print("Failed")


"""
Fixed using the in operator
"""

name = "James"
if name in ("Jim", "Fred"):
    print("Welcome")
else:
    print("Failed")

"""
Another possible fix would be
explicitly comparing the variable to each string
"""
name = "James"
if name == "Jim" or name == "Fred":
    print("Welcome")
else:
    print("Failed")
