def print3(w):
	i=0
	while i<w:
		print "dashabi"
		i+=1
print "zhengheming"
print3(1)
print "shine?"
s=6
print3(s+3)
print "jiushi"
print "--------------------------------"
def countSubChar(s,ch):
	c=0
	i=0
	while i<len(s):
		if s[i]==ch:
			c+=1
		i+=1
	print c,ch
s1="hello jeapedu.com"
cc="e"
countSubChar(s1,cc)
print "--------------------------------"
def countSubstring():
	i=0
	while i<=len(s)-len(sub):
		if s[i:i+len(sub)]==sub:
			print i,s[i:i+len(sub)],s
		i+=1
s="hello"
sub="ll"
countSubstring()
print "--------------------------------"
def myfind(s):
	i=0
	while i<=len(s)-len(sub):
		if s[i:i+len(sub)]==sub:
			print i
			break
		i+=1
	else:
		print -1
s="hello jeapedu.com"
sub="jeap"
myfind(s)
print "--------------------------------"
def myFindmax(s):
	max=0
	for x in s:
		if x>max:
			max=x
	print 'max',max
s=[1,2,31,4,52,6,7,8,55,23]
myFindmax(s)
print "--------------------------------"
def findlistmax():
    i = 0
    m = 0
    while i < len(l):
        if l[i] > m:
            m = l[i]
        i+=1
    print m
l = [1,2,7,3,4,1105,5,10,6,7,8105,9]
findlistmax()
print "--------------------------------"
def myFindmax(s):
	max=0
	max2=0
	for x in s:
		if x>max:
			max2=max
			max=x
		else:
			if x>max2 and x!=max:
				max2=x
	print 'max',max,'max2',max2
s=[1,2,31,44,5,6,7,8,55,55,23]
myFindmax(s)
print "--------------------------------"
def myfindmax():
    i = 0
    max = 0
    max2 = 0
    while i < len(l):
        if max < l[i]:
        	max2=max
            	max = l[i]	
        else:
        	if max2<l[i] and l[i]!=max:
        		max2 = l[i]
        i+=1
    print 'max',max,'max2',max2
l=[1,56,56,8,82,1,6,34]
myfindmax()