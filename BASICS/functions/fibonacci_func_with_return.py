# define function

def fib(n):

	"""Return a list containing the Fibonacci series up to n"""

	result = []
	a, b = 0, 1

	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

num = int(input("Enter a positive Number:\n"))
print(fib(num))
