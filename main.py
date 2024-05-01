import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
image= Image.open('test.png')

text = pytesseract.image_to_string(image)

print(text)