import re
regx = "[a-z]+[A-Z]{3}[a-z][A-Z]{3}[a-z]+"
regx1 = "[A-Z]{3}[a-z][A-Z]{3}"
s1 = ""
cnt = 0
with open("pythonChallengeText4.txt") as fp:
	for eachline in fp.readlines():
        	temp = re.findall(regx,eachline)
	        cnt += 1
	        if temp:
		        	print "[%d] %s"%(cnt,temp)
		        	for val in temp:
		        			for x in re.findall(regx1,val):
		        				s1 += x[3]		           
print s1