# -*- coding:utf-8 -*-
import re,os
import zipfile as zp
PATH = "/Users/cc/Desktop"
os.chdir(PATH)          #将工作目录转至所下载zip的文件目录

def getEnd(nums,z):
    """
    利用递归的方法,读取压缩包内每个文件,
    直至找到内容不一样的文件,返回该文件名
    """
    global l1
    filename = nums+".txt"
    target = z.read(filename)
    l1.append(z.getinfo(filename).comment)
    if "Next nothing is " in target:
        val = re.search("\d+",target).group()
        return getEnd(val,z)
    else:
        print z.read(filename)
        return filename

if __name__=="__main__":
    global l1
    l1 = []
    z = zp.ZipFile("pythonChallenge6.zip")
    tar = getEnd("90052",z)
    print z.read(tar)
    s1 = ""
    for x in l1:
        s1 += x
    print s1
