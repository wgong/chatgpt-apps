import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Notepad")

# Create a text widget and place it in the main window
text = tk.Text(window)
text.pack()

# Create a function to save the text in the text widget to a file
def save_text():
    text_content = text.get("1.0", "end")
    with open("notes.txt", "w") as f:
        f.write(text_content)

# Create a function to open a text file and load its contents into the text widget
def open_text():
    with open("notes.txt", "r") as f:
        text_content = f.read()
        text.delete("1.0", "end")
        text.insert("1.0", text_content)

# Create a function to clear the contents of the text widget
def clear_text():
    text.delete("1.0", "end")


# Create a save button and place it in the main window
save_button = tk.Button(window, text="Save", command=save_text)
save_button.pack()


# Create the menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create the File menu
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_text)
file_menu.add_command(label="Save", command=save_text)

# Create the Edit menu
edit_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_text)

# Run the main loop
window.mainloop()
