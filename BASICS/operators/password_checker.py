password = "Tr0ubador"
length = len(password)
has_digits = any(char.isdigit() for char in password)

if length >= 8 and has_digits:
	print("Moderate Strength")
elif length >= 8 or has_digits:
	print("Weak, but has some merit")
else:
	print("Very Weak")

