import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# im = Image.open("surat.png") # the second one 
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('surat.png')
text = pytesseract.image_to_string(Image.open('surat-izin.jpg'), lang='ind')
print(text)