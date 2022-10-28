# ------------------------------------------------------------------------------------------------
# Import

import png
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# ------------------------------------------------------------------------------------------------
# Set up the QRCode Generator

url = input("Input URL Address : ")
image_names = "myqrcode.png"
img = pyqrcode.create(url)
img.png(image_names, scale = 6)

# Decoded Pyzbar Method 1
d = decode(Image.open(image_names))
decode = (d[0].data.decode("ascii"))
print("Decoded QR Code to ASCII : ", decode)

# Decoded Pyzbar Method 2
"""
    for obj in decode:
        print("Data : ", obj.data)
"""