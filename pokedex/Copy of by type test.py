import tkinter as tk
from tkinter import ttk

# Create a function to handle option selection
def handle_selection(event):
    selected_option = combo_box.get()
    print("Selected option:", selected_option)

# Create the main Tkinter window
root = tk.Tk()
root.title("Option Box Example")

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])

# Set default value
combo_box.set("Select an option")

# Bind an event to handle option selection
combo_box.bind("<<ComboboxSelected>>", handle_selection)

# Place the Combobox widget on the window
combo_box.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()