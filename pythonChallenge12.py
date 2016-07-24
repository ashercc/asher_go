#-*- coding:utf-8 -*-
from PIL import Image
from urllib import urlretrieve

with open('evil2.gfx', 'rb') as inFile:
    data = inFile.read()

for i in range(5):
    with open(str(i), 'wb') as outFile:
        outFile.write(data[i::5])
