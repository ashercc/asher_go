# -*- coding:utf-8 -*-
#http://www.pythonchallenge.com/pc/def/channel.html
from zipfile import ZipFile
from urllib import urlretrieve
from re import search
import sys,string
# urlretrieve("http://www.pythonchallenge.com/pc/def/channel.zip","channel.zip")
zp = ZipFile("channel.zip")
namelist = zp.namelist()
regx = "\d+$"
for x in namelist:
    if 'readme.txt' in x:
        print zp.read(x)
    zp.read(x)
    print zp.comment
comments = []
def getFile(num):
    global comments
    filename = num + ".txt"
    temp = zp.read(filename)
    m = search(regx,temp)
    comments.append(zp.getinfo(filename).comment)
    if m is None:
        print zp.read(filename)
        return num
    else:
        getFile(m.group())

if __name__=="__main__":
    getFile("90052")
    target = ''
    for x in comments:
        if x in string.letters and x not in target:
            target += x
    print target,'\n'
