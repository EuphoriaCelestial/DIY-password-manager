import keyboard
from Xlib import X, display


def get_current_window_id():
    root = display.Display().screen().root
    window_id = root.get_full_property(display.XInternAtom(display.Display(), "_NET_ACTIVE_WINDOW", 0), 0).value[0]
    return window_id


class StringSearch:
    def __init__(self, string_list):
        self.string_list = string_list

    def search_suggestions(self, query):
        query = query.lower()
        suggestions = [string for string in self.string_list if query in string.lower()]
        return suggestions


# Example usage:
string_list = ["apple", "banana", "orange", "grape", "pear", "pineapple"]
search_engine = StringSearch(string_list)

user_input = ""
while True:
    current_window_id = get_current_window_id()

    # Check if the active window is your application window
    if current_window_id == get_current_window_id():
        print(f"Current input: {user_input}")

        suggestions = search_engine.search_suggestions(user_input)

        if suggestions:
            print("Suggestions:", suggestions)
        else:
            print("No matches found.")

        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_DOWN:
            if key_event.name == 'enter':
                break
            elif key_event.name == 'backspace':
                user_input = user_input[:-1]
            elif key_event.name.isalnum() or key_event.name.isspace():
                user_input += key_event.name
    else:
        # Your application is not in focus; you can add other actions or sleep here
        pass
