import pytesseract
from PIL import Image
from googletrans import Translator
import tkinter as tk

# Set the Tesseract executable path (adjust this path to your Tesseract installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Function to display the translated text in an overlay window
def display_translated_text(translation_en):
    # Create a tkinter main window
    root = tk.Tk()

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window just above the Start menu
    window_width = 1000  # Adjust as needed
    window_height = 200  # Adjust as needed
    x_position = (screen_width - window_width) // 2
    y_position = screen_height - window_height - 100  # 40 pixels above the Start menu

    # Create a label with the translated text and specified font
    label = tk.Label(root, text=translation_en, font=("Forte", 60), fg='black')

    # Set window attributes
    label.master.overrideredirect(True)  # Hide window borders and title bar
    label.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Set window position
    label.master.lift()                   # Bring the window to the front
    label.master.attributes("-topmost", True)  # Keep the window on top of others
    label.master.attributes("-disabled", True)  # Disable the window interaction
    label.master.attributes("-transparentcolor", "white")  # Make the background white transparent

    # Schedule window destruction after 2000 milliseconds (approximately 2 seconds)
    label.after(3000, root.destroy)
    label.pack()

    # Start the tkinter main loop
    root.mainloop()



# Load the image
image_path = 'test.png'  # Replace with the path to your image
image = Image.open(image_path)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image, lang='jpn')  # Use 'eng' for English

# Print the extracted text
print(f'Extracted text: {extracted_text}')

translator = Translator()
translation_en = translator.translate(extracted_text, dest="en").text


display_translated_text(translation_en)

# Print the translated text
print(f'Translated text: {translation_en}')
