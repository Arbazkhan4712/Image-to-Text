import pytesseract #pip install tesseract
import os
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #Path to the tesseract 

img = Image.open('img.jpg')# add Image name here with file extention
text = pytesseract.image_to_string(img)
print(text)
remember = open('remember.txt','w')
remember.write(text)
remember.close()
