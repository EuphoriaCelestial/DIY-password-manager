import hashlib


def hash_string(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Create a SHA3-256 hash object
    sha3_256_hash = hashlib.sha3_256()

    # Update the hash object with the input bytes
    sha3_256_hash.update(input_bytes)

    # Get the hexadecimal representation of the hash
    hashed_string = sha3_256_hash.hexdigest()

    return hashed_string


if __name__ == "__main__":
    # Example usage:
    input_string = "test test"
    hashed_result = hash_string(input_string)
    print(f"Hashed result: {hashed_result}")
