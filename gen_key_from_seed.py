import hashlib
import random


def generate_AES_key(seed):
    # Set the seed for the random module
    random.seed(seed)

    # Generate a random 32-byte key
    random_key = ''.join([chr(random.randint(0, 255)) for _ in range(32)])

    # # Hash the random key to ensure a consistent length of 32 bytes
    deterministic_key = hashlib.md5(random_key.encode('utf-8')).hexdigest()

    return deterministic_key


if __name__ == "__main__":
    # Example usage:
    seed_value = "test test"  # Replace with your desired seed value
    generated_key = generate_AES_key(seed_value)

    print(f"Generated 32-byte key with seed {seed_value}: {generated_key}")
