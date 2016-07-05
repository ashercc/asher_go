# -*- coding:utf-8 -*-
# 看到这张图片,感觉中间那个黑白条像条形码一样
import os,re
from PIL import Image
PATH = "/Users/cc/Desktop"
os.chdir(PATH)
im = Image.open("pc7.png")
pixels = im.getdata()
print im.getdata(),len(pixels)
print im.size,im.mode
print im.info
lim = im.convert('L')
print lim.getdata(),len(lim.getdata()),lim.mode
pixel = lim.getdata()
l1 = []
for x in range(0,lim.width,7):
    val = pixel[x]
    l1.append(val)
print l1
s1 = ""
for x in l1:
    s1 += chr(x)
print s1
s2 = ""
for x in re.findall("\d+",s1):
    s2 += chr(int(x))
print s2