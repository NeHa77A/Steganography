from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import os
from stegano import lsb

def make_circular(image_path, size):
    image = Image.open(image_path).resize(size).convert("RGBA")
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    result = Image.new("RGBA", size)
    result.paste(image, (0, 0), mask=mask)
    return result

def showImage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                          filetypes=(("PNG file", "*.png"), ("JPG File", "*.jpg"), ("All File", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img

def Hide():
    global secret1
    message = text1.get(1.0, END)
    img = Image.open(filename)
    img = img.convert("RGB")  # Convert image to RGB mode
    secret1 = lsb.hide(img, message)


def Show():
    clear_mess = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_mess)

def Save():
    global secret1
    if secret1 is not None:
        secret1.save("hidden.png")

root = Tk()
root.title("Steganography - Secret message hidden in Image")
root.geometry("750x500+150+180")
root.resizable(False, False)
root.configure(bg="#50DBB4")

# icon
image_icon = make_circular("logo.png", (50, 50))
photo_icon = ImageTk.PhotoImage(image_icon)

root.iconphoto(False, photo_icon)

# logo
logo_image = make_circular("logo1.png", (70, 70))
logo = ImageTk.PhotoImage(logo_image)

label_logo_frame = Frame(root, bg="#50DBB4")
label_logo_frame.place(x=10, y=5)
label_logo = Label(label_logo_frame, image=logo, bg="#50DBB4")
label_logo.pack()

Label(root, text="CYBER SCIENCE", bg="#50DBB4", fg="black", font=("Arial", 25, "bold")).place(x=100, y=20)

## first Frame ---> Photo Section
frame1 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
frame1.place(x=10, y=90)

lbl = Label(frame1, bg="black")
lbl.place(x=40, y=7)

# Second frame ---> Textarea
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=370, y=90)

text1 = Text(frame2, font="Robote 20", bg="white", fg="black", relief=GROOVE)
text1.place(x=0, y=0, width=320, height=290)

Scrollbar1 = Scrollbar(frame2)
Scrollbar1.place(x=320, y=0, height=300)
text1.configure(yscrollcommand=Scrollbar1.set)

## Third Frame
frame3 = Frame(root, bd=3, bg="#50DBB4", width=340, height=100, relief=GROOVE)
frame3.place(x=10, y=380)
Button(frame3, text="Open Image", width=10, height=2, font="arial 12 bold", command=showImage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 12 bold", command=Save).place(x=180, y=30)
Label(frame3, text="Picture Image, Photo File", bg="#50DBB4", fg="blue", font="Robote 10 bold").place(x=20, y=7)

## Fourth Frame --->For the textarea
frame4 = Frame(root, bd=3, bg="#50DBB4", width=340, height=100, relief=GROOVE)
frame4.place(x=373, y=380)
Button(frame4, text="Hide Mess", width=10, height=2, font="arial 12 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Mess", width=10, height=2, font="arial 12 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Data That is Hidden", bg="#50DBB4", fg="blue", font="Robote 10 bold").place(x=20, y=7)

root.mainloop()
