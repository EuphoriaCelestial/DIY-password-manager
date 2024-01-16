import sys

from gen_key_from_seed import generate_AES_key
from passphrase_parser import *
from user_choice_processor import save_login_info, read_login_info


def main():
    # Ask user for secret pass phrase
    # secret_phrase = parser()
    # if not secret_phrase:
    #     sys.exit()
    secret_phrase = "strongest_pass"  # test mode (change to the actual strongest pass to run, this is for Git submit)

    # Generate private key for AES
    private_key = generate_AES_key(secret_phrase)

    while True:
        choice = input("Do you want to: \n"
                       "1. Save new login info \n"
                       "2. Read saved logins \n"
                       "3. Search for a specific login \n"
                       "4. Exit the program")

        if choice == '1':
            save_login_info(private_key)
        elif choice == '2':
            read_login_info(None, private_key)
        elif choice == '3':
            query = input("Search for: ")
            read_login_info(query, private_key)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
