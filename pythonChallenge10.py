# -*- coding:utf-8 -*-
from urllib import urlretrieve
from PIL import Image,ImageDraw
from re import findall
# urlretrieve("http://www.pythonchallenge.com/pc/return/bull.jpg","bull.jpg")
# s1 = '146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399'
# tmp = s1.split(',')
# coords = []
# for x in tmp:
#     coords.append(int(x))
# print coords
# img = Image.open("bull.jpg")
# draw = ImageDraw.Draw(img)
# for x in range(0,len(coords)-3):
#     draw.line(coords[x:x+4],fill="red")
# img.show()
# urlretrieve("http://www.pythonchallenge.com/pc/return/sequence.txt","sequence10.txt")
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,num):
        self.stack.append(num)
        return len(self.stack)
    def pop(self):
        self.stack.pop()
        return len(self.stack)
    def getTop(self):
        return len(self.stack)
    def getTopVar(self):
        return self.stack[-1]
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def clear(self):
        self.stack = []
        print "stack cleared..."

def doSeq(s1):
    ss = ""
    cnt = 0
    flag = False
    tmp = s1[cnt:]
    var = s1[cnt]
    while flag or tmp:
        if st.isEmpty():
            st.push(var)
            cnt += 1
        elif not st.isEmpty() and var==st.getTopVar():
            st.push(var)
            cnt += 1
        else:
            a = "%s"%st.getTop()
            b = st.getTopVar()
            ss += a+b
            st.clear()
            flag = False
            if var=='*':
                break
        if cnt==len(s1):
            flag = True
        if cnt<len(s1):
            var = s1[cnt]
        else:
            var = '*'
        tmp = s1[cnt:]

    return ss

with open("sequence10.txt") as fp:
    s1 = fp.read()
    regx = '\d+'
    seq = findall(regx,s1)
    print seq
    global st
    st = Stack()
    l1 = ['111221']
    loop = 0
    while loop<26:
        l1.append(doSeq(l1[-1]))
        loop += 1
    print len(l1[-1])




# Regular Expression Solutions
#
# Here's a short & sweet way to get the whole job done, exploiting that regexps have a natural way to say "find the longest sequence starting at the current position consisting of repetitions of the current digit". The "(\d)" matches a digit as group #1, and the "\1" matches the same thing as group #1. Group #0, or m.group(0), is the entire string.
#
# import re
# def describe(s):
#     return "".join([str(len(m.group(0))) + m.group(1)
#                     for m in re.finditer(r"(\d)\1*", s)])
# s = "1"
# for dummy in range(30):
#     s = describe(s)
# print len(s)  # prints 5808
#
# Here's another version of the regular expression portion, broken into two lines. This shows there are multiple ways to write this, and usually a concise way without explicit for loops.
#
# def describe(s):
#     sets = re.findall("(1+|2+|3+)", s)  # like "111", "2", ...
#     return "".join([str(len(x))+x[0] for x in sets])
