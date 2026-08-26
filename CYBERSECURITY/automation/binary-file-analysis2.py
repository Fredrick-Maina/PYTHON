python3 << 'EOF'
import lief
import json

binary = lief.parse("beacon.bin")

# Get dynamic entries (correct way for LIEF)
print("=== DYNAMIC ENTRIES ===")
for entry in binary.dynamic_entries:
    print(f"{entry.tag.name}: {entry.value}")

# Get symbols
print("\n=== SYMBOLS ===")
for symbol in binary.symbols:
    print(f"{symbol.name}")

# Get sections
print("\n=== SECTIONS ===")
for section in binary.sections:
    print(f"{section.name}: size={section.size}, virtual_size={section.virtual_size}")

# Get segments
print("\n=== SEGMENTS ===")
for segment in binary.segments:
    print(f"Segment: virtual_address=0x{segment.virtual_address:x}, size={segment.physical_size}")
EOF
