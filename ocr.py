def ocrConvert(location):


    import pytesseract
    from PIL import Image

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    image= Image.open(location)
    # image.save('Capture.jpeg')

    text = pytesseract.image_to_string(image)

    return text