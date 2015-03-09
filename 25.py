s="aa bb cc aa dd ee aa"
sub="aa"
def mycount():
	i=0
	r=0
	while i<len(s):
		if s[i:i+len(sub)]==sub:
			print i
			r+=1
		i+=1
	print "num",r
mycount()
print "------------------------------"
s="aa bb cc aa dd ee aa"
sb="aa"
def myfind(sub):
	i=0
	while i<len(s):
		if s[i:i+len(sub)]==sub:
			print '->',i
		i+=1
myfind(sb)
print "------------------------------"
s = "aa bb cc aa dd ee aa ff"
sub = "aa"
def findsse(a,b,start = 0,end = 0):
	i = start 
	if end == 0:
		end = len(a)
	print 'i->',i,'start->',start,'end->',end
	while  i < end -len(b):
		if a[i:i+len(b)]==b:
			return i
		i+=1
	return -1
	#return c 
r = findsse(s,sub)
print r
r = findsse(s,sub,5)
print r
r = findsse(s,sub,5,12)
print r
print "------------------------------"
import random
a=[]
i=0
while i<10:
	a.append(random.randint(1,5))
	i+=1
print a
temp=[]
for x in a:
	if x not in temp:
		temp.append(x)
print temp
for x in temp:
	if temp.count(x)!=1:
		print 'num->',temp.count(x)
print "-------------------------------"
li1=range(1,11)
li2=range(2,15)
pos=li1.index(10)+1
print pos
i=0
while i<len(li2):
	li1.insert(pos,li2[len(li2)-(i+1)])
	print i+1,'->',li1 
	i+=1
print "-------------------------------"