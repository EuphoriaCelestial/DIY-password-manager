from logger import append_to_json, read_from_json
from configs import LOGBOOK
from crypto_core import encrypt, decrypt


def save_login_info(private_key):
    # User input
    pass_name = input("Enter ID for this login: ")
    login = input("Enter the login: ")
    password = input("Enter the password: ")
    other_info = input("Additional info? ")

    # Encrypt the data
    encrypted_login = encrypt(login, private_key)
    encrypted_pass = encrypt(password, private_key)
    encrypted_info = encrypt(other_info, private_key)

    # Pack to dictionary
    encrypted_data = {pass_name: {
        "login": encrypted_login,
        "password": encrypted_pass,
        "other_info": encrypted_info,
        }
    }

    # Save file
    append_to_json(LOGBOOK, encrypted_data)
    print(f"Saved")


def read_login_info(query, private_key):
    encrypted_data = read_from_json(query, LOGBOOK)
    decrypted_data = {}

    if encrypted_data is not None:
        for category, content in encrypted_data.items():
            decrypted_content = {}
            for field, encrypted_value in content.items():
                decrypted_value = decrypt(encrypted_value, private_key)
                decrypted_content[field] = decrypted_value
            decrypted_data[category] = decrypted_content
    else:
        decrypted_data['result'] = "No result found"

    print(decrypted_data['result'])
