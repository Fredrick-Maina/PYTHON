"""
	make sure your env satisifies this dependencies, lief and json
	you can install lief in venv using pip3 install lief
"""

import lief
import json

binary = lief.parse("fileName.bin")

# Get all strings
print("=== STRINGS ===")
for s in binary.strings:
    if len(s) > 4:
        print(s)

# Get imported functions
print("\n=== IMPORTS ===")
for lib in binary.imports:
    print(f"\nLibrary: {lib.name}")
    for func in lib.entries:
        print(f"  {func.name}")

# Get sections
print("\n=== SECTIONS ===")
for section in binary.sections:
    print(f"{section.name}: {section.size} bytes, flags: {section.characteristics}")
