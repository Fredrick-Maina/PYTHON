for n in range (2,10):
	for x in range(2,n):
		if n % x == 0:
			print(f"{n} is equals to {x} * {n//x}")
			break

# the break statement breaks out of the innermost enclosing for loop
