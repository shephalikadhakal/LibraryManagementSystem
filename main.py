from addBook import *
from viewBook import *
from issue import *
from delete import *
from returnbook import *
from tkinter import *
from tkinter import Canvas
from constant import data
from bg_const import bg_data
import PIL
from tkinter import *
from tkinter import Canvas
import PIL
from PIL import ImageTk, Image

import base64
import io
# Designing the window
root = Tk()
img = PhotoImage(data=data)
root.iconphoto(False,img)
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("1020x735")

# Add Background Image
image_data = base64.b64decode(bg_data)
stream=io.BytesIO(image_data)
bg = Image.open(stream)


def resize_image(event):
    width = event.width
    height = event.height
    image = bg.resize((width,height),Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0,0,image=photo,anchor='nw')
    canvas.image = photo

# create a canvas
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Create a canvas
canvas = Canvas(root, width=windowWidth, height=windowHeight)
canvas.pack(fill="both", expand=True)
canvas.bind('<Configure>', resize_image)

# add the heading
head = Frame(root,bg="yellow",bd=5)
head.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headLabel = Label(head, text="Welcome to the Library", bg='black', fg='white', font=('Courier',20))
headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# adding the buttons
b1 = Button(root, text="Add Book", bg='black', activebackground='#e7e7e7', fg='white', font=('Courier New', 16),command=addBook)
b1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
b2 = Button(root, text="Delete Book", bg='black', activebackground='#e7e7e7', fg='white', font=('Courier New', 16),command=delete)
b2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
b3 = Button(root, text="View Books", bg='black', activebackground='#e7e7e7', fg='white', font=('Courier New', 16),command=View)
b3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)
b4 = Button(root, text="Issue Book", bg='black', activebackground='#e7e7e7', fg='white', font=('Courier New', 16),command=issue)
b4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)
b5 = Button(root, text="Return Book", bg='black', activebackground='#e7e7e7', fg='white', font=('Courier New', 16),command=returnBook)
b5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()