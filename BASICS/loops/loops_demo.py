# loops_demo.py - for Loops, while Loops, range(), break, and continue
# Run this script and study each section's output.

# ===========================
# Part 1: for loop over a list
# ===========================

print("=" * 40)
print("FOR LOOP OVER A LIST")
print("=" * 40)

targets = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for ip in targets:
    print(f"Scanning {ip}...")

# ===========================
# Part 2: for loop over a string
# ===========================

print("\n" + "=" * 40)
print("FOR LOOP OVER A STRING")
print("=" * 40)

password = "S3cure!"

for char in password:
    if char.isdigit():
        print(f"  Found digit: {char}")
    elif char.isupper():
        print(f"  Found uppercase: {char}")
    elif char.islower():
        print(f"  Found lowercase: {char}")
    else:
        print(f"  Found special: {char}")

# ===========================
# Part 3: range() function
# ===========================

print("\n" + "=" * 40)
print("RANGE EXAMPLES")
print("=" * 40)

print("range(5):")
for i in range(5):
    print(f"  {i}", end="")
print()   # newline

print("range(1, 6):")
for i in range(1, 6):
    print(f"  {i}", end="")
print()

# ===========================
# Part 4: break and continue
# ===========================

print("\n" + "=" * 40)
print("BREAK EXAMPLE")
print("=" * 40)

for port in [22, 80, 443, 8080]:
    if port == 443:
        print(f"Port {port} found. Stopping scan.")
        break
    print(f"Checked port {port}")

print("\n" + "=" * 40)
print("CONTINUE EXAMPLE")
print("=" * 40)

lines = ["admin", "", "root", "", "guest"]

for line in lines:
    if line == "":
        continue
    print(f"Processing: {line}")

# ===========================
# Part 5: Dictionary iteration
# ===========================

print("\n" + "=" * 40)
print("DICTIONARY ITERATION")
print("=" * 40)

services = {22: "SSH", 80: "HTTP", 443: "HTTPS"}

for port, name in services.items():
    print(f"Port {port} = {name}")

# ===========================
# Part 6: range() with three arguments
# ===========================

print("\n" + "=" * 40)
print("RANGE WITH THREE ARGUMENTS")
print("=" * 40)

print("Counting by fives from 0 to 45:")
for i in range(0, 50, 5):
    print(f"  {i}", end="")
print()
