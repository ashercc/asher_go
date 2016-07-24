# -*- coding:utf-8 -*-
from urllib import urlretrieve
from PIL import Image
# urlretrieve("http://www.pythonchallenge.com/pc/return/cave.jpg","cave11.jpg")
img = Image.open("cave11.jpg")
img1 = Image.new(img.mode,(img.size[0]/2,img.size[1]/2))
img2 = Image.new(img.mode,(img.size[0]/2,img.size[1]/2))
for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        img1.putpixel((x,y),img.getpixel((x*2,y*2)))
        img2.putpixel((x,y),img.getpixel((x*2+1,y*2+1)))
img1.show()
img2.convert('L')
img2.show()
img1.save('cave_even.jpg')
