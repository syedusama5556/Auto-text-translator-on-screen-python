import tkinter as tk

# Function to close the tkinter window
def close_window():
    root.destroy()

# Create a tkinter main window
root = tk.Tk()
root.title("Test Window")

# Create a label with some text
label = tk.Label(root, text="This window will close in 5 seconds")
label.pack(padx=20, pady=20)

# Schedule window destruction after 5000 milliseconds (5 seconds)
root.after(5000, close_window)

# Start the tkinter main loop
root.mainloop()
