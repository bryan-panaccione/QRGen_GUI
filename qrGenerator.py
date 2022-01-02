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
from tkinter import ttk


#####################################################################
# define window, tabs, title
#####################################################################

root = tk.Tk()
root.title('QR Code Generator, 1/3d CR')
# create window
root.geometry("1000x563")
# set minimum window size value
root.minsize(1000, 563)
# set maximum window size value
root.maxsize(1000, 563)
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Create New QR Code')
tabControl.add(tab2, text='Edit Previous')
tabControl.add(tab3, text='View All')
tabControl.pack(expand=1, fill="both")

#####################################################################
# Shared elements
#####################################################################

# Unique Logo
tigerImage = PIL.Image.open(r'C:\Users\Owner\Pictures\tigerLogo2.png')
tigerPhoto = ImageTk.PhotoImage(tigerImage)
customLogo = Label(image=tigerPhoto)
customLogo.place(relx=0.395, rely=0.65)

#####################################################################
# TAB 1 Elements and Functions
#####################################################################
# Select Center Logo
logo_choice = StringVar(tab1, "1")
choices = {"Tiger Symbol": '1', "3CR Bug": '2', "Sabres": '3', "None": '4'}
countRadios = 0.2

for (text, value) in choices.items():
    Radiobutton(tab1, text=text, variable=logo_choice,
                value=value).place(relx=0.7, rely=countRadios)
    countRadios = countRadios + 0.075


class pathLabelControl:
    def __init__(self, path):
        self.path_selected = Label(tab1, text=path, font=("Arial", 10))

    def adderPath(self):
        self.path_selected.place(relx=0.52, rely=0.41)

    def removerPath(self):
        self.path_selected.place_forget()


def pickAPath():
    global file_path
    global showpath
    file_path = filedialog.askdirectory()
    showpath = pathLabelControl(file_path)
    showpath.adderPath()


def generateQR(inputURL, nameSave, chosenLogo):
    # tack-on 8 digit unique identifier
    random8 = random.randint(00000000, 99999999)
    # get radio button logo selection
    if (chosenLogo == '1'):
        logo = PIL.Image.open(
            r'C:\Users\Owner\Documents\PythonDemos\tigerLogo.png')
    if (chosenLogo == '2'):
        logo = PIL.Image.open(
            r'C:\Users\Owner\Documents\PythonDemos\tinyLogo.png')
    # this method works, for none, figure out if easy to bypass steps or make image a black square
    # resize logo
    #logo = PIL.Image.open(r'C:\Users\Owner\Documents\PythonDemos\tigerLogo.png')
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
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white').convert('RGB')
    # overlay logo center of qr code
    qrWidth, qrHeight = img.size
    logo_x = int((qrWidth/2) - (basewidth/2))
    logo_y = int((qrHeight/2) - (hsize/2))
    PIL.Image.Image.paste(img, logo, (logo_x, logo_y))
    # save and show QR Code
    checkPath = pathlib.Path(f'{file_path}/My_QRcodes')
    if checkPath.exists():
        img.save(f"{file_path}/My_QRcodes/{nameSave}_{random8}.png", quality=100)
    else:
        os.mkdir(f'{file_path}/My_QRcodes')
        img.save(f"{file_path}/My_QRcodes/{nameSave}_{random8}.png", quality=100)
    img.show()
    print(f"Successful QR Code Creation,  Image saved to: {file_path}")
    print(logo_choice)


# required to get input information in correct format
url_var = tk.StringVar()
name_var = tk.StringVar()


def create():
    chosenLogo = logo_choice.get()
    nameSave = name_var.get()
    inputURL = url_var.get()
    generateQR(inputURL, nameSave, chosenLogo)
    url_input.delete(0, END)
    save_input.delete(0, END)
    showpath.removerPath()


# User Input Fields
url_input = tk.Entry(tab1, textvariable=url_var,
                     relief="sunken", border="5", width="35")
save_input = tk.Entry(tab1, textvariable=name_var,
                      relief="sunken", border="5", width="35")
path_browse = tk.Button(tab1, text="Browse...",
                        relief="raised", border="5", bg="#dbe2ff", command=pickAPath)
# Labels (excluding selected path label, located in pathlabelcontrol class)
page_label = Label(tab1, text="Create a New QR Code",
                   font=("Cooper Black", 22))
url_label = Label(tab1, text="QR Code links to:", font=("Arial", 16))
save_label = Label(tab1, text="Save QR Code As:", font=("Arial", 16))
path_label = Label(tab1, text="Local Save Location:", font=("Arial", 16))
radio_label = Label(tab1, text="Add Logo", font=("Cooper Black", 16))
courtesyOf = Label(
    tab1, text="Created by CPT Bryan Panaccione, to resolve problems with this software, email bp@rqpcreative.com", font=("Bradley Hand ITC", 12))
# Create Button, takes all input data
createQR_btn = tk.Button(tab1, text="Create QR Code!",
                         relief="raised", border="3", fg="white", bg="#096114", command=create)

# Placed location all elements, would prefer to use grid but it was acting weird.
page_label.place(relx=0.2, rely=0.05)
url_label.place(relx=0.2, rely=0.2)
save_label.place(relx=0.2, rely=0.3)
path_label.place(relx=0.2, rely=0.4)
url_input.place(relx=0.4, rely=0.2)
save_input.place(relx=0.4, rely=0.3)
path_browse.place(relx=0.43, rely=0.4)
createQR_btn.place(relx=0.43, rely=0.55)
courtesyOf.place(relx=0, rely=0.95)
radio_label.place(relx=0.7, rely=0.13)

#####################################################################
# TAB 2 Elements and Functions
#####################################################################


#####################################################################
# TAB 3 Elements and Functions
#####################################################################


root.mainloop()
