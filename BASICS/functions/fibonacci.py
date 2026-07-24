def fib(n): # write Fibonacci Series less than n
	"""Print a Fibonacci series less than n"""
	a, b = 0, 1
	while a<n:
		print(a, end = '...')
		a, b = b, a + b
	print()


while True:
	n = int(input("\nPlease enter a positiver number:\n"))
	if n>0:
		break
	print("That is a negative number.")
fib(n)

# input() always returns a string, so using int() we convert the string to an integer.
