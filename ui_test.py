import tkinter as tk


def on_button_click():
    label.config(text="Button clicked!")


# Create the main window
window = tk.Tk()
window.title("Sample Python UI")

# Create a button
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Create a label
label = tk.Label(window, text="Welcome to the Python UI")
label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
