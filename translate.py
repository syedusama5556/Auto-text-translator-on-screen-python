import pytesseract
import pyautogui
import re
from PIL import Image
from googletrans import Translator
import tkinter as tk
import keyboard

# Set the Tesseract executable path (adjust this path to your Tesseract installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Function to display the translated text in an overlay window with dynamic dimensions and text wrapping
def display_translated_text(translation_en):
    # Create a tkinter main window
    root = tk.Tk()

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window just above the Start menu
    window_width = 0.8 * screen_width  # Adjust as needed
    window_height = 0.1 * screen_height  # Adjust as needed
    x_position = int((screen_width - window_width) // 2)
    y_position = int(screen_height - window_height - 100)  # 40 pixels above the Start menu

    # Create a label with the translated text and specified font
    label = tk.Label(root, text=translation_en, font=("Arial", 35), fg='black', wraplength=window_width)

    # Set window attributes
    label.master.overrideredirect(True)  # Hide window borders and title bar
    label.master.geometry(f"{int(window_width)}x{int(window_height)}+{x_position}+{y_position}")  # Set window position

    label.master.lift()                   # Bring the window to the front
    label.master.attributes("-topmost", True)  # Keep the window on top of others
    label.master.attributes("-disabled", True)  # Disable the window interaction
    label.master.attributes("-transparentcolor", "white")  # Make the background white transparent

    # Schedule window destruction after 5 seconds
    label.after(5000, root.destroy)
    label.pack()

    # Start the tkinter main loop
    root.mainloop()


# Define the region to capture (adjust as needed)
capture_region = (0, 0, 2413, 1332)  # Captures a limited area (300 pixels in height)

# Use a flag to track if 't' key is pressed
t_pressed = False
processing = False

# Initialize a variable to store all the extracted Japanese text
all_japanese_text = ""

# Function to handle 't' key press event
def on_t_key_event(e):
    global t_pressed, processing, all_japanese_text
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 't' and not processing:
            t_pressed = True
            processing = True
    elif e.event_type == keyboard.KEY_UP:
        if e.name == 't':
            t_pressed = False

keyboard.on_press_key('t', on_t_key_event)  # Register 't' key press event

# Add a delay to control the frequency of screen captures
print('Running in BG')

while True:
    try:
        # Check if 't' key is pressed
        if t_pressed:
            # Capture a screenshot of the specified region
            screenshot = pyautogui.screenshot(region=capture_region)

            # Use pytesseract to extract text from the screenshot
            extracted_text = pytesseract.image_to_string(screenshot, lang='jpn')

            # Combined regex pattern for matching both Kanji and Hiragana/Katakana
            combined_pattern = r'([一-龯ぁ-んァ-ン]+)'

            # Compile the combined regular expression
            combined_regex = re.compile(combined_pattern, re.UNICODE)

            # Find all matches in the extracted text
            matches = combined_regex.findall(extracted_text)

            if matches:
                print("Matches:")
                for match in matches:
                    japanese_text = match
                    print(f'Found JA text: {japanese_text}')

                    # Add the extracted Japanese text to the combined text
                    all_japanese_text += japanese_text + " "

                # Initialize the translator
                translator = Translator()

                # Translate the combined Japanese text to English
                translation = translator.translate(all_japanese_text, src='ja', dest='en')
                translated_text = translation.text
                print(f'Translated text EN: {translated_text}')

                # Create a text widget on the canvas with dynamic dimensions
                display_translated_text(translated_text)
                pyautogui.sleep(1)

            t_pressed = False  # Reset 't' key flag after processing
            processing = False

    except Exception as e:
        print(f"Error: {str(e)}")
