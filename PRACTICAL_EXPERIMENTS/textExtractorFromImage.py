from PIL import Image
import pytessaract

# if you don't have pytessaract installed, use: "python3 -m pip install pytessaract pillow"

text = pytesseract.image_to_string(Image.open("/Path/to/image"))
print(text)
