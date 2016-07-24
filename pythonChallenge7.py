# -*- coding:utf-8 -*-
from urllib import urlretrieve
from PIL import Image
import sys
urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png","oxygen.png")
img = Image.open("oxygen.png")
width,height = img.size
print "width = ",width
print "height = ",height
# 43-53，0-607
img1 = img.crop((0,43,607,53)).convert("L")
s1 = ""
for x in range(img1.size[0]):
    s1 += chr(int(img1.getpixel((x,5))))
cnt = 0
s2 = ""
for x in s1:
    cnt += 1
    if cnt==7:
        s2 += x
        cnt = 0
l1 = s2[42:-1].split(",")
for x in l1:
    sys.stdout.write(chr(int(x.strip())))
