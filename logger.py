import json


def append_to_json(filename, new_data):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except:
        data = {}

    for data_id, encrypted_message in new_data.items():
        while data_id in data:
            choice = input(f"ID '{data_id}' already exists. Do you want to overwrite? (y/n): ").lower()
            if choice == 'y':
                break
            else:
                data_id = input("Enter a new ID to save the data: ")

        data[data_id] = encrypted_message

    with open(filename, 'w') as file:
        json.dump(data, file)


def read_from_json(query, filename):
    try:
        with open(filename, 'r') as file:
            encrypted_data = json.load(file)

        if query is None:
            # return all content
            return encrypted_data
        else:
            # return just 1 record user searched for
            if query in encrypted_data:
                return {"result": encrypted_data[query]}
            else:
                return None
    except FileNotFoundError:
        return {}

