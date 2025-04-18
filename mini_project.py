from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

# Global variable to hold the image filename
filename = None

def showimage():
    global filename  # Ensure filename is accessible globally
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select Image File',
                                           filetypes=(("PNG file", "*.png"),
                                                     ("JPG file", "*.jpg"),
                                                     ("All file", "*.*")))
    if filename:  # Check if a file was selected
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img

def Hide():
    global filename
    message = text1.get(1.0, END)
    if filename:  # Ensure the filename exists
        secret = lsb.hide(filename, message)
        secret.save("hidden.png")

from tkinter import simpledialog, messagebox

def Show():
    global filename
    if filename:  # Ensure the filename exists
        # Ask the user to enter the passcode
        code = simpledialog.askstring("Authentication Required", "Enter the passcode:")
        if code == "1234":
            clear_message = lsb.reveal(filename)
            if clear_message:
                text1.delete(1.0, END)
                text1.insert(END, clear_message)
            else:
                messagebox.showerror("Error", "No hidden message found.")
        else:
            messagebox.showerror("Authentication Failed", "Incorrect passcode. Access denied.")


def save():
    global filename
    if filename:
        secret = lsb.hide(filename, text1.get(1.0, END))
        secret.save("hidden.png")


# Icon
image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)

# Logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# First frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# Second frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# Third frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)


# Fourth frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
