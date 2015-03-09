s0="hello"
s1='jeapedu'
s2=""".com"""
s3='''www.'''
s4='''hello
jeapedu'''
print s0
print s1
print s2
print s3
print s4
print "--------------------------"
i=0
s="jeapedu"
f="0"
h="00"
while i<=100:
	if i<10:
		print s+h+str(i)
	else:
		if i==100:
			print s+str(i)
		else:
			print s+f+str(i)
	i+=1
print "-----------------------------"
s="abcdefghijklmnopqrstuvwxyz"*56
i=0
a=0
while i<len(s):
	if s[i]=="g":
		print s[i],i,
		a=a+1
		print a
	i+=1
print "---------------------------"
import random
a=(random.randint(100000,1000000))
s=str (a)
q=1
while q<5:
	a=(random.randint(100000,1000000))
	s=str (a)
	if "4" in s or "7" in s:
		print s
		i=0
		while i<len(s):
			if s[i]=="4" or s[i]=="7":
				print i,s[i]
			i=i+1
	q=q+1
print "---------------------------------"
x=97
i=0
f="0"
while i<26:
	s=chr(x+i)
	if i<9:
		print s+f+str(i+1),
	else:
		print s+str(i+1),
	i+=1