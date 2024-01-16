import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt(message, key):
    message = pad(message)
    key = key.encode('utf-8')

    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)

    backend = default_backend()

    # Use AES-256 with GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=backend)
    encryptor = cipher.encryptor()

    # Encrypt the message
    ct = encryptor.update(message.encode('utf-8')) + encryptor.finalize()

    # Get the authentication tag
    tag = encryptor.tag

    # Combine IV, ciphertext, and tag for the final result
    encrypted_result = iv + ct + tag

    return base64.b64encode(encrypted_result).decode('utf-8')


def decrypt(ciphertext, key):
    key = key.encode('utf-8')

    # Decode the base64 encoded ciphertext
    encrypted_result = base64.b64decode(ciphertext)

    # Extract IV, ciphertext, and tag from the combined result
    iv = encrypted_result[:16]
    ct = encrypted_result[16:-16]
    tag = encrypted_result[-16:]

    backend = default_backend()

    # Use AES-256 with GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=backend)
    decryptor = cipher.decryptor()

    # Decrypt the message
    decrypted_text = decryptor.update(ct) + decryptor.finalize()

    return decrypted_text.decode('utf-8').rstrip()


def pad(s):
    return s + (32 - len(s) % 32) * chr(32 - len(s) % 32)
