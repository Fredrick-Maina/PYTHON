import qrcode
import qrcode.image.svg as qr
import os

s = input("Enter the website/words you want to create QR Code for: ")

q = qrcode.QRCode(version=1, box_size=10, border=5)

q.add_data(s)
q.make(fit=True)

img = q.make_image(fill_color="black", back_color="white")

if not os.path.exists("static"):
    os.makedirs("static")

# saving the file in the Static folder

file_path = os.path.join("static", "qrcode.jpg")
img.save(file_path)

# displaying the absolute path dynamically
absolute_path = os.path.abspath(file_path)
print(f"Image saved at: {absolute_path}")

# if you want to use a backward slash, the usage needs to be a raw string:
# r"static\qrcode.jpg"
