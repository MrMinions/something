li1=range(1,11)
li2=range(2,15)
pos=li1.index(6)
i=0
while i<len(li2):
	li1.insert(pos,li2[len(li2)-(i+1)])
	print i+1,'->',li1 
	i+=1
print "-----------------------------------"
li1=range(1,11)
li2=range(2,15)
pos=li1.index(6)
i=len(li2)-1
while i>0:
	li1.insert(pos,li2[i])
	print '->',li1
	i-=1
print "-----------------------------------"
li1=range(1,11)
li2=range(2,15)
i=0
while i<len(li2):
	s=li2[i]
	li1.append(s)
	i+=1
print li1
print "-----------------------------------"
s=[1,2,3,1,1,2,3,1,2,2,2,3,1,3]
i=0
while i<len(s):
	if s.count(s[i])>1:
		print s[i],'->',s.pop(s.index(s[i]))
		i-=1
	i+=1
print s
print "---------------------------------"
s=[1,2,3,1,1,2,3,1,2,2,2,3,1,3]
i=0
x=10
while i<s.count(2):
	s.remove(2)
	i+=1
print s