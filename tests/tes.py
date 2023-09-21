import tkinter as tk

# Define a function 'text' that takes an argument 'n'
def text(n):


    # Create a label with some text and specified font
    label = tk.Label(text=str(n), font="Arial 60", bg='white', fg='black')

    # Set window attributes
    label.master.overrideredirect(True)  # Hide window borders and title bar
    label.master.geometry("+512+312")     # Set window position
    label.master.lift()                   # Bring the window to the front
    label.master.attributes("-topmost", True)  # Keep the window on top of others
    label.master.attributes("-disabled", True)  # Disable the window interaction
    label.master.attributes("-transparentcolor", "white")  # Make the background white transparent

    # Schedule window destruction after 1006 milliseconds (approximately 1 second)
    label.after(2000, label.master.destroy)
    label.pack()

# Example usage of the 'text' function
text("Hello, World!")

# Start the tkinter main loop
tk.mainloop()
