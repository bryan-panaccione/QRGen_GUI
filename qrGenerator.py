import qrcode
import PIL.Image
from PIL import ImageTk
# import PIL
import os
import pathlib
from tkinter import *
import random
import tkinter as tk
from tkinter import filedialog

# root = tk.Tk()

# path = filedialog.askdirectory(initialdir="/", title="Select file")
# print(path)

# root.mainloop()
# def main():
#   ffffff
# this will be primary function eventually

###################################################
# the following functions define user interface and collect inputs
###################################################
# def userInterface():

root = tk.Tk()
root.title('QR Code Generator, 1/3d CR')
# create window
root.geometry("1000x563")
# set minimum window size value
root.minsize(1000, 563)
# set maximum window size value
root.maxsize(1000, 563)
# action functions

# get the path they want to save to


def pickAPath():
    global file_path, path_selected
    file_path = filedialog.askdirectory()
    path_selected = Label(root, text=file_path, font=(
        "Arial", 10), bg="white", width=50).place(relx=0.5, rely=0.46)


# get the URL they want to link to
url_var = tk.StringVar()


def getURL():
    global inputURL
    inputURL = url_var.get()


# get the name they want to save it as
name_var = tk.StringVar()


def workingQR(inputURL, nameSave):
    #inputURL = "https://www.google.com/"
    # generate random 8 digit tag for files
    random8 = random.randint(00000000, 99999999)
    # resize logo
    logo = PIL.Image.open(r'C:\Users\Owner\Pictures\tinyLogo.jpg')
    basewidth = 50
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo.thumbnail((basewidth, hsize), PIL.Image.ANTIALIAS)
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
    PIL.Image.Image.paste(img, logo, (logo_x, logo_y))
    # save and show QR Code
    #image_path = r'C:\Users\Owner\Documents\My_QRcodes'
    checkPath = pathlib.Path(f'{file_path}/My_QRcodes')
    checkPrevious = pathlib.Path(
        f'{file_path}/{nameSave}{random8}.png')
    if checkPrevious.exists():
        random8 = random8 + '(002)'
    if checkPath.exists():
        img.save(f"{file_path}/My_QRcodes/{nameSave}{random8}.png", quality=100)
    else:
        os.mkdir(f'{file_path}/My_QRcodes')
        img.save(f"{file_path}/My_QRcodes/{nameSave}{random8}.png", quality=100)
    img.show()
    print(f"Successful QR Code Creation,  Image saved to: {file_path}")


def create():
    nameSave = name_var.get()
    inputURL = url_var.get()
    workingQR(inputURL, nameSave)
    url_input.delete(0, END)
    save_input.delete(0, END)


# Header
createTab = tk.Button(root, text="Create QR Code", fg="black",
                      bg="#607c8c", font=("Arial", 28))
editTab = tk.Button(root, text="Edit QR Code", fg="black",
                    bg="#607c8c", font=("Arial", 28), width=17)
viewTab = tk.Button(root, text="Saved QR Codes", fg="black",
                    bg="#607c8c", font=("Arial", 28))

# Input Fields - URL, Save As, Select a Filepath, Browse file paths button
url_input = tk.Entry(root, textvariable=url_var,
                     relief="sunken", border="5", width="35")
save_input = tk.Entry(root, textvariable=name_var,
                      relief="sunken", border="5", width="35")
path_browse = tk.Button(root, text="Browse...",
                        relief="raised", border="5", bg="#dbe2ff", command=pickAPath)
# Input labels - Link QR Code to: , Save QR Code as: , Save Location:
page_label = Label(root, text="Create a New QR Code",
                   font=("Cooper Black", 18))
url_label = Label(root, text="QR Code links to:", font=("Arial", 16))
save_label = Label(root, text="Save QR Code As:", font=("Arial", 16))
path_label = Label(root, text="Local Save Location:", font=("Arial", 16))

# Custom Logo
tigerImage = PIL.Image.open(r'C:\Users\Owner\Pictures\tigerLogo2.png')
tigerPhoto = ImageTk.PhotoImage(tigerImage)
customLogo = Label(image=tigerPhoto)
courtesyOf = Label(
    root, text="Created by CPT Bryan Panaccione", font=("Bradley Hand ITC", 10))
# Create Button
createQR_btn = tk.Button(root, text="Create QR Code!",
                         relief="raised", border="3", fg="white", bg="#096114", command=create)

# Grid location all elements
page_label.place(relx=0.1, rely=0.15)
createTab.place(relx=0.0, rely=0)
editTab.place(relx=0.3, rely=0)
viewTab.place(relx=0.67, rely=0)
url_label.place(relx=0.1, rely=0.25)
save_label.place(relx=0.1, rely=0.35)
path_label.place(relx=0.1, rely=0.45)
url_input.place(relx=0.4, rely=0.25)
save_input.place(relx=0.4, rely=0.35)
path_browse.place(relx=0.4, rely=0.45)
createQR_btn.place(relx=0.43, rely=0.6)
customLogo.place(relx=0.395, rely=0.65)
courtesyOf.place(relx=0, rely=0.95)

# select file path to save QR Codes


# print(file_path)
# path = filedialog.askdirectory(initialdir="/", title="Select file")
# print(path)


################################################
# the following functions create QRcodes IAW inputs from the user
###############################################

# ignore this for now
# def customQR(inputURL, fill, image_path, showOrSave):


# This is the working QR function with values hard coded in for testing


# def test():


# dynamic functionality is based on databases, use AWS S3 buckets for a specific link generated by a QR code. Program needs to create a new S3 bucket?


# workingQR()
root.mainloop()
