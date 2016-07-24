# -*- coding:utf-8 -*-
import urllib2,re,sys

def getTheEnd(nums):
	site = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nums
	page = urllib2.urlopen(site).read()
	if not re.search("\d+$",page):
		print "Done...%s"%site
		sys.exit(0)
	else:
		print "[%s] [%s] \n   %s"%(nums,page,site)
		getTheEnd(page.split(' ')[-1])

if __name__ == '__main__':
	getTheEnd('83287')