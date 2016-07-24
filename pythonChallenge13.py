# -*- coding:utf-8 -*-
from PIL import ImageDraw,Image
from urllib import urlretrieve
# urlretrieve("http://www.pythonchallenge.com/pc/return/disprop.jpg","disprop13.jpg")
print "Done"
img = Image.open("disprop13.jpg")
img2 = img.convert('RGB')
print img2.getpixel((326,177))
draw = ImageDraw.Draw(img2)
draw.ellipse([326,177,45,105],fill="blue",outline="red")
draw.line([326,177,45,105],fill="red",width=2)
img2.show()
