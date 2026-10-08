import re

INPUT_FILE = "input.txt"
XOR_KEY = 0x5A

def extract_encoded_bytes(file_path):
    values = []
    with open(file_path) as f:
        for line in f:
            stripped = line.strip()
            if not stripped.startswith("local_38"):
                continue
            match = re.search(r"=\s*(0x[0-9a-fA-F]+|\d+)\s*;", stripped)
            if match:
                values.append(int(match.group(1), 0))

    if not values:
        raise ValueError(
            f"No 'local_38[...] = ...;' lines found in {file_path}. "
            "Make sure you pasted the raw decompiled data in the file."
        )
    return values


def decode(encoded_bytes, key):
    return "".join(chr(b ^ key) for b in encoded_bytes)


if __name__ == "__main__":
    encoded = extract_encoded_bytes(INPUT_FILE)
    print(f"Extracted {len(encoded)} bytes: {encoded}")
    print(f"Decoded flag: {decode(encoded, XOR_KEY)}")
        
