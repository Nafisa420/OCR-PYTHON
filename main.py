from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pyttsx3

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

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    image= Image.open(data[0])
    text = pytesseract.image_to_string(image)

    e1.insert(END,text)

# Text-to-Speech
def convertToSpeech():
    if not e1.get("1.0", "end-1c"):
        messagebox.showwarning("Warning", "No text to convert to speech.")
        return

    converter = pyttsx3.init()
    voices = converter.getProperty('voices')
    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    converter.setProperty('voice', voice_id)
    converter.say(e1.get("1.0", "end-1c"))
    # converter.save_to_file(e1.get("1.0", "end-1c"), 'speech.mp3')
    converter.runAndWait()

# save  mp3
# def saveMp3():
#     if not e1.get("1.0", "end-1c"):
#         messagebox.showwarning("Warning", "No text to convert to speech.")
#         return

#     converter = pyttsx3.init()
#     voices = converter.getProperty('voices')
#     voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
#     converter.setProperty('voice', voice_id)
#     # converter.say(e1.get("1.0", "end-1c"))
#     converter.save_to_file(e1.get("1.0", "end-1c"), 'speech.mp3')
#     converter.runAndWait()


# gui

b1=ttk.Button(app,text="Browse",command=browseFile)
b1.pack()

b2=ttk.Button(app,text="Convert",command=convertFile)
b2.pack()

b3 = ttk.Button(app, text="Convert to Speech", command=convertToSpeech)
b3.pack()

e1=Text(app, yscrollcommand = scrollbar.set, xscrollcommand = scrollbarH.set)
e1.pack()

scrollbar.config( command = e1.yview)
scrollbarH.config( command = e1.xview)

app.mainloop()
