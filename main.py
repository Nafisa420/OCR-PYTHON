from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

# Storing location in data
data = [""]

# app

app = Tk()
app.title("OCR-Python")

# vertical scrollbar
scrollbar = Scrollbar(app)
scrollbar.pack(side = RIGHT, fill=Y)

# horizontal scrollbar
scrollbarH = Scrollbar(app,orient=HORIZONTAL)
scrollbarH.pack(side = BOTTOM, fill=X)


# File Browsing

def browseFile():

    s_files = [".jpg", ".JPG",
               ".jpeg", ".JPEG",
               ".png", ".PNG",]
    
    filename = askopenfilename(filetypes=[("Image Files", tuple(["*" + item for item in s_files]))])
    
    data[0]=filename
    e1.delete('1.0', END)

# Converting image to text

def convertFile():
    
    import pytesseract
    from PIL import Image

    if data[0]=="":
        messagebox.showwarning("showwarning", "Please select file.")
        return

    pytesseract.pytesseract.tesseract_cmd = r'resources\Tesseract-OCR\tesseract'

    image= Image.open(data[0])
    text = pytesseract.image_to_string(image)

    e1.insert(END,text)


# gui

b1=ttk.Button(app,text="Browse",command=browseFile)
b1.pack()

b2=ttk.Button(app,text="Convert",command=convertFile)
b2.pack()

e1=Text(app, yscrollcommand = scrollbar.set, xscrollcommand = scrollbarH.set)
e1.pack()

scrollbar.config( command = e1.yview)
scrollbarH.config( command = e1.xview)

app.mainloop()
