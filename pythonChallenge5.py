import pickle,urllib

def fun(a):
    print a[0]*a[1]
# urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/banner.p","banner.p")
pickle.load(open("banner.p"))
object = pickle.load(open("banner.p"))
for item in object:
    print "".join(map(lambda p: p[0]*p[1], item))
