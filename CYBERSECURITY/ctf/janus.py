# janus on 31 nights of r00t by https://dojo.africahackon.com

def decode(data_hex, key_hex):
    data = bytes.fromhex(data_hex)
    key = bytes.fromhex(key_hex)
    return bytes(b ^ key[i % len(key)]
                 for i, b in enumerate(data))

validator_data = (
    "acf09dcaa5aa99d0abb3f28dbcf7cf8d"
    "e9a69bdce9a19c8eefa4958bedf49b89"
    "ebf0cec3"
)

checker_data = (
    "8df6959684ac918c8ab5fa8f8ab29196"
    "cca2fad1c7a5c681c6fe91d0c7f590da"
    "cba7c0d099f091dacaf5c49f"
)

print("Validator:", decode(validator_data, "dec0adbe").decode())
print("Checker:  ", decode(checker_data, "ffc6a5e2").decode())
