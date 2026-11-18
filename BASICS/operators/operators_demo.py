# operators_demo.py - Arithmetic and Membership Operators
# Run this script to see each operator in action.

print("=" * 40)
print("ARITHMETIC OPERATORS")
print("=" * 40)

# Basic operators (review)
print(f"10 + 3  = {10 + 3}")
print(f"10 - 3  = {10 - 3}")
print(f"10 * 3  = {10 * 3}")
print(f"10 / 3  = {10 / 3}")

# New operators
print(f"\n--- Floor Division (//): divides and rounds down ---")
print(f"10 // 3 = {10 // 3}")
print(f"7 // 2  = {7 // 2}")

print(f"\n--- Modulus (%): returns the remainder ---")
print(f"10 % 3  = {10 % 3}")
print(f"7 % 2   = {7 % 2}")
print(f"255 % 16 = {255 % 16}")
print(f"100 % 10 = {100 % 10}")

# Even/odd check using modulus
number = 42
if number % 2 == 0:
    print(f"\n{number} is even")
else:
    print(f"\n{number} is odd")

print(f"\n--- Exponent (**): raises to a power ---")
print(f"2 ** 8   = {2 ** 8}")
print(f"2 ** 10  = {2 ** 10}")
print(f"5 ** 2   = {5 ** 2}")

# Security context: key sizes
print(f"\nA 16-bit key has {2 ** 16} possible values")
print(f"A 32-bit key has {2 ** 32} possible values")

print("\n" + "=" * 40)
print("MEMBERSHIP OPERATORS (in / not in)")
print("=" * 40)

common = ["123456", "password", "qwerty", "letmein"]

test1 = "qwerty"
test2 = "S3cure!Pass"

print(f"\nCommon passwords: {common}")
print(f"'{test1}' in common:     {test1 in common}")
print(f"'{test2}' in common:     {test2 in common}")
print(f"'{test2}' not in common: {test2 not in common}")

# in operator with strings
url = "https://tryhackme.com/room/pythonbasics"
print(f"\n'tryhackme' in url: {'tryhackme' in url}")
print(f"'hackthebox' in url: {'hackthebox' in url}")
