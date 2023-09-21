import pytesseract

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Update this path to your Tesseract installation location

# Test Tesseract installation
try:
    version_info = pytesseract.get_tesseract_version()
    print(f"Tesseract OCR Version: {version_info}")
except Exception as e:
    print(f"Error: {str(e)}")

# Now you can use pytesseract for text extraction
