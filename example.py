import pytesseract
from PIL import Image
import os, os.path

# path joining version for other paths
DIR = 'img'
countfiles = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
onlyfiles = os.listdir(DIR)

# convert all img files into txt using forloop
for i in range(countfiles):
    imgpath = DIR+"/"+onlyfiles[i]
    text = pytesseract.image_to_string(Image.open(imgpath), lang='ind')
    print(text)
    print("============================================")

# converting process to txt
# text = pytesseract.image_to_string(Image.open('img/surat-izin.jpg'), lang='ind')
# print(text)