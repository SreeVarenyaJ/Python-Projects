import cv2
import pytesseract
import re

# Path to the PAN card image
image_path = r"C:\Users\Sreelu\OneDrive\Documents\New folder\pancardexample.jpeg"

# Read the image of the PAN card
image = cv2.imread(image_path)

# Convert the image to string using pytesseract
text = pytesseract.image_to_string(image)

# Regular expression to match the PAN card number format
pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

# Search for the PAN card number in the extracted text
match = pattern.search(text)

# Print the PAN card number if found, else print an empty string
if match:
    print("PAN Card Number:", match.group())
else:
    print("")


