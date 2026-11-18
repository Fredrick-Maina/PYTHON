# lists_dicts_demo.py - Lists and Dictionaries
# Run this script and study the output.
# Then try adding your own port-service pair to the services dictionary.

# ===========================
# Part 1: Lists
# ===========================

print("=" * 40)
print("LISTS")
print("=" * 40)

ports = [22, 80, 443, 8080]
print(f"Original list: {ports}")
print(f"First element: {ports[0]}")
print(f"Last element:  {ports[-1]}")
print(f"Slice [1:3]:   {ports[1:3]}")
print(f"Length:         {len(ports)}")

# Modifying a list
ports.append(3306)
print(f"\nAfter append(3306):  {ports}")

ports.remove(8080)
print(f"After remove(8080):  {ports}")

ports.sort()
print(f"After sort():        {ports}")

# The in operator
print(f"\n22 in ports:   {22 in ports}")
print(f"9999 in ports: {9999 in ports}")

# Common passwords list
common_passwords = ["123456", "password", "admin", "letmein", "qwerty"]
test_pw = "admin"
print(f"\nIs '{test_pw}' in common_passwords? {test_pw in common_passwords}")

# ===========================
# Part 2: Dictionaries
# ===========================

print("\n" + "=" * 40)
print("DICTIONARIES")
print("=" * 40)

services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}
print(f"Original dict: {services}")
print(f"services[22]:  {services[22]}")
print(f"services[443]: {services[443]}")

# Adding an entry
services[8080] = "HTTP-Alt"
print(f"\nAfter adding 8080: {services}")

# Updating an entry
services[22] = "OpenSSH"
print(f"After updating 22: {services}")

# Removing an entry
del services[3306]
print(f"After deleting 3306: {services}")

# Checking for keys
print(f"\n80 in services:   {80 in services}")
print(f"9999 in services: {9999 in services}")

# The .get() method with a fallback
result = services.get(9999, "Unknown")
print(f"services.get(9999, 'Unknown'): {result}")

# Dictionary methods
print(f"\nKeys:   {list(services.keys())}")
print(f"Values: {list(services.values())}")

# Final state
print(f"\nFinal dictionary: {services}")
print(f"Number of items:  {len(services)}")
