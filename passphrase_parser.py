import getpass

from hash_passphrase import hash_string
from configs import *


def parser():
    n_try = 0
    while True:
        secret_phrase = getpass.getpass("Welcome! Enter your secret pass phrase to start: ")
        hashed_sec_phrase = hash_string(secret_phrase)

        if hashed_sec_phrase == STORED_PASS_PHRASE:
            return secret_phrase
        else:
            n_try += 1

        if n_try == 3:
            return False
