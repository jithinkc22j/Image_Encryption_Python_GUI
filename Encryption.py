import time
import tkinter as jk
from tkinter import *
from tkinter import Menu
from tkinter import filedialog
import PIL
# importing Image class from PIL package
import cv2
import numpy as np
# importing Image class from PIL package
from PIL import Image
from PIL import ImageTk
from numpy import asarray

# --------------------------------------------------------------

# Functions
# --------------------------------------------------------------
pivot = 0
mj = 0
wi = 0
he = 0
# ---------------------------------------------------------------
# Browse a file
# -------------------------------------------------------------


def ct():
    cap = cv2.VideoCapture('jj.mp4')

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error opening video file")

    # Read until video is completed
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:

            # Display the resulting frame
            cv2.imshow('Getscriptall-Image Encryption', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

        # Break the loop
        else:
            cv2.destroyAllWindows()
            break

        # When everything done, release

    # Closes all the frames
    cv2.destroyAllWindows()


def s(e1):
    global mj
    m = e1.get()
    print(float(m))
    mj = float(m)
    label6 = jk.Label(root, text='logistic map selected, press Encryption/Decryption', fg='green', width=50,
                      font=('helvetica', 8, 'bold', 'italic'))
    canvas1.create_window(420, 180, window=label6)


def cli():
    global wi, he
    image_file_location = filedialog.askopenfilename(initialdir="C:/Users/%s")
    img = PIL.Image.open(image_file_location)
    img.save('plain.png')
    wi, he = img.size
    print(wi, he)
    time.sleep(2)
    canvas1.image = ImageTk.PhotoImage(img.resize((200, 200), Image.ANTIALIAS))
    # canvas.image = ImageTk.PhotoImage(img)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    label3 = jk.Label(root, text='Plain image successfully updated', fg='green', font=('helvetica', 8, 'bold'), width=30
                      )
    canvas1.create_window(110, 220, window=label3)
    label7 = jk.Label(root, text='Please Select a Chaotic map', fg='green', font=('helvetica', 8, 'bold', 'italic'),
                      width=50)
    canvas1.create_window(420, 180, window=label7)


# -----------------------------------------------------------------------------------------
# Main- Encryption /Decryption function:
# ---------------------------------------------------------------

def encryption():

    if pivot == 1:
        mapv = logistic()
        le(mapv)
        label7 = jk.Label(root, text='select the map and press Decryption button', fg='green',
                          font=('helvetica', 8, 'bold', 'italic'), width=50)
        canvas1.create_window(420, 180, window=label7)


def decryption():
    if pivot == 1:
        mapv = logistic()
        dle(mapv)
        label8 = jk.Label(root, text='select the map and press Encryption button', fg='green', width=50,
                          font=('helvetica', 8, 'bold', 'italic'))
        canvas1.create_window(420, 180, window=label8)


# ------------------------------------------------------------
# Maps Encryption function:
# ------------------------------------------------------------
def le(mapv):
    global wi, he
    time.sleep(2)
    imag = PIL.Image.open("plain.png")
    print(wi, he)
    im1 = imag.getchannel(0)
    im2 = imag.getchannel(1)
    im3 = imag.getchannel(2)
    im1 = asarray(im1)
    im2 = asarray(im2)
    im3 = asarray(im3)
    imn1 = np.zeros((wi, he), dtype='uint8')
    imn2 = np.zeros((wi, he), dtype='uint8')
    imn3 = np.zeros((wi, he), dtype='uint8')
    print(mapv.size)
    for i in range(he-1):
        for j in range(wi-1):
            imn1[i][j] = im1[i][j] ^ mapv[i][j]
            imn2[i][j] = im2[i][j] ^ mapv[i][j]
            imn3[i][j] = im3[i][j] ^ mapv[i][j]
    imp1 = Image.fromarray(imn1, mode='L')
    print(imp1.size)
    imp2 = Image.fromarray(imn2, mode='L')
    imp3 = Image.fromarray(imn3, mode='L')
    # merge
    merged = Image.merge("RGB", (imp1, imp2, imp3))
    # merged.show(title='output')
    # output = 6 ^ 3
    # print(output)
    merged.save("cipher.png")
    print(merged.size)
    time.sleep(2)
    merged = PIL.Image.open("cipher.png")
    wi, he = merged.size
    canvas1.image = ImageTk.PhotoImage(merged.resize((200, 200), Image.ANTIALIAS))
    # canvas1.image = ImageTk.PhotoImage(merged)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    label4 = jk.Label(root, text='Cipher image successfully updated  ', fg='green', font=('helvetica', 8, 'bold'),
                      width=30)
    canvas1.create_window(110, 220, window=label4)


# ------------------------------------------------------------
# Maps Decryption function:
# ------------------------------------------------------------


def dle(mapv):
    global wi, he
    time.sleep(2)
    imag = PIL.Image.open("cipher.png")
    print(imag.size)
    im11 = imag.getchannel(0)
    im22 = imag.getchannel(1)
    im33 = imag.getchannel(2)
    im1 = np.asarray(im11)
    im2 = np.asarray(im22)
    im3 = np.asarray(im33)
    imn1 = np.zeros((wi, he), dtype='uint8')
    imn2 = np.zeros((wi, he), dtype='uint8')
    imn3 = np.zeros((wi, he), dtype='uint8')
    print(mapv.size)
    for i in range(he - 1):
        for j in range(wi - 1):
            imn1[i][j] = im1[i][j] ^ mapv[i][j]
            imn2[i][j] = im2[i][j] ^ mapv[i][j]
            imn3[i][j] = im3[i][j] ^ mapv[i][j]
    imp1 = Image.fromarray(imn1, mode='L')
    imp2 = Image.fromarray(imn2, mode='L')
    imp3 = Image.fromarray(imn3, mode='L')
    # merge
    merged = Image.merge("RGB", (imp1, imp2, imp3))
    # merged.show(title='output')
    # output = 6 ^ 3
    # print(output)
    merged.save('decipher.png')
    print(merged.size)
    time.sleep(2)
    merged = PIL.Image.open('decipher.png')
    [wi, he] = merged.size
    canvas1.image = ImageTk.PhotoImage(merged.resize((200, 200), Image.ANTIALIAS))
    # canvas1.image = ImageTk.PhotoImage(merged)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    label4 = jk.Label(root, text='Decrypted image successfully updated ', fg='green', font=('helvetica', 8, 'bold'),
                      width=30)
    canvas1.create_window(110, 220, window=label4)


# ---------------------------------------------------------------
# Chaotic map selection function:
# ---------------------------------------------------------------
def maps(c):
    global pivot
    if c == 1:
        pivot = 1
        par()
    if c == 2:
        pivot = 2
        label6 = jk.Label(root, text='Arnold map selected, press Encryption/Decryption', fg='green', width=50,
                          font=('helvetica', 8, 'bold', 'italic'))
        canvas1.create_window(420, 180, window=label6)

    return pivot


# ---------------------------------------------------------------
# Chaotic maps function:
# ---------------------------------------------------------------


def logistic():
    global mj, wi, he
    print(wi, he)
    logi = np.zeros((wi, he), dtype='float')
    x = mj
    r = 4
    for i in range((he-1)):
        for j in range(wi-1):
            logi[i][j] = r * x * (1 - x)
            x = logi[i][j]

    logis = np.zeros((wi, he), dtype='uint8')
    for i in range(he-1):
        for j in range(wi-1):
            logis[i][j] = (logi[i][j] * 10000) % 256
    return logis


# -------------------------------------------------------
# Main function
# -------------------------------------------------------


root = jk.Tk()
ct()

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open", command=lambda: cli())
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

file.add_separator()
file.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)

root.config(menu=menubar)

canvas1 = Canvas(root, width=1290, height=1290, bg="orange red")
canvas1.create_line(0, 250, 1290, 250, dash=(255, 255))
canvas1.create_line(235, 10, 1290, 10, dash=(255, 255))
canvas1.create_line(235, 80, 1290, 80, dash=(255, 255))
canvas1.create_line(235, 10, 1290, 1100000, dash=(255, 255))
canvas1.create_line(0, 290, 1290, 290, dash=(255, 255))
canvas1.create_line(0, 340, 1290, 340, dash=(255, 255))
canvas1.pack()


# -------------------------------------------------------
# Buttons :
# -------------------------------------------------------


def par():
    label5 = jk.Label(root, text='Enter your secret key and click save', fg='green', font=('helvetica', 8, 'bold',
                                                                                           'italic'), width=50)
    canvas1.create_window(420, 180, window=label5)
    # key = jk.StringVar()
    key = jk.IntVar()
    e1 = jk.Entry(root, bd=5, show="", textvariable=key)
    e1.place(x=250, y=205)

    button10 = jk.Button(text='save', bg='olive drab', fg='white', width=22, command=lambda: s(e1))
    canvas1.create_window(470, 220, window=button10)


button1 = jk.Button(text='Decryption', command=lambda: decryption(), bg='dark green', fg='white', width=22)
canvas1.create_window(500, 60, window=button1)
button2 = jk.Button(text='Encryption', command=encryption(), bg='dark green', fg='white', width=22)
canvas1.create_window(320, 60, window=button2)
button3 = jk.Button(text='Logistic Chaotic Map', bg='olive drab', fg='white', width=22)
button3["command"] = lambda: maps(1)
canvas1.create_window(320, 320, window=button3)
button5 = jk.Button(text='Arnold Chaotic Map', command=lambda: encryption(), bg='olive drab', fg='white', width=22)
canvas1.create_window(500, 320, window=button5)
button6 = jk.Button(text='Henon Chaotic Map', command=lambda: encryption(), bg='olive drab', fg='white', width=22)
canvas1.create_window(140, 320, window=button6)
button7 = jk.Button(text='Logistic Chaotic Map', bg='olive drab', fg='white', width=22)
button7["command"] = lambda: maps(1)
canvas1.create_window(320, 270, window=button7)
button8 = jk.Button(text='Arnold Chaotic Map', command=lambda: encryption(), bg='olive drab', fg='white', width=22)
canvas1.create_window(500, 270, window=button8)
button9 = jk.Button(text='Henon Chaotic Map', command=lambda: encryption(), bg='olive drab', fg='white', width=22)
canvas1.create_window(140, 270, window=button9)

# -------------------------------------------------------
# Labels :
# -------------------------------------------------------

root.mainloop()
