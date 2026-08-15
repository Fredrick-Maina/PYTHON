"""
list comprehensions provide a concise way to create lists.
common applications are to make new lsits where each element is the reuslt of some operatoin applied to
each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a
certain condition.

example illustration:
"""
squares = []

for x in range(10):
	squares.append(x**2)

# uncomment this if you are running as a file
# print(squares) 

# uncomment this if you are using the python interpreter on the Command Line
# squares
