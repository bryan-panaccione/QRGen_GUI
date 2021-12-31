import qrcode
from PIL import Image
#import PIL
import os
import pathlib
import tkinter
import random


# def main():
#   print('big balls')
# this will be primary function eventually

###################################################
# the following functions define user interface and collect inputs
###################################################
# def userInterface():


################################################
# the following functions create QRcodes IAW inputs from the user
###############################################
def customQR(inputURL, fill, image_path, showOrSave):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(inputURL)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color='white')
    checkPath = pathlib.Path(image_path)
    # img.open(r'Documents\My QR Codes\')
    if showOrSave == True:
        img.show()
        return
    elif checkPath.exists():
        img.save(f"{image_path}/newQRcode3.png")
    else:
        os.mkdir(image_path)
        img.save(f"{image_path}/newQRcode3.png")
    print(f"Successful QR Code Creation, Image saved to: {image_path}")

# This is the working QR function with values hard coded in for testing


# def test():


# use add and clear somehow to alter input QR codes?


def workingQR():
    inputURL = "https://www.google.com/"
    # generate random 8 digit tag for files
    random8 = random.randint(00000000, 99999999)
    # resize logo
    logo = Image.open(r'C:\Users\Owner\Pictures\tinyLogo.jpg')
    basewidth = 50
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo.thumbnail((basewidth, hsize), Image.ANTIALIAS)
    # create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(inputURL)
    # qr.clear()
    # qr.add_data("https://www.brigadeoutfitters.com")
    qr.make(fit=True)
    # must convert to rgb so logo doesnt look funky
    img = qr.make_image(fill_color='black', back_color='white').convert('RGB')
    # overlay logo center of qr code
    qrWidth, qrHeight = img.size
    logo_x = int((qrWidth/2) - (basewidth/2))
    logo_y = int((qrHeight/2) - (hsize/2))
    Image.Image.paste(img, logo, (logo_x, logo_y))
    # save and show QR Code
    image_path = r'C:\Users\Owner\Documents\My_QRcodes'
    checkPath = pathlib.Path(r'C:\Users\Owner\Documents\My_QRcodes')
    checkPrevious = pathlib.Path(
        f'C:\\Users\\Owner\\Documents\\My_QRcodes\\newQRcode{random8}.png')
    if checkPrevious.exists():
        random8 = random8 + '(002)'
    if checkPath.exists():
        img.save(f"{image_path}/newQRcode{random8}.png", quality=100)
    else:
        os.mkdir(image_path)
        img.save(f"{image_path}/newQRcode{random8}.png", quality=100)
    img.show()
    print(f"Successful QR Code Creation,  Image saved to: {image_path}")

# changeQRcodeData-Dynamic function


workingQR()
