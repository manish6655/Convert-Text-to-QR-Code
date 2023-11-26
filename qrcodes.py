import os
os.system('pip install qrcode')
import qrcode

manish = input("Enter Your Barcode Words:")
img = qrcode.make(manish)
img.save("myQrcode.jpg")

