def sub(time):
	global c
	c+=1
	print 'c=',c
	print time
	for x in range(0,time):
		print "hello"
c=0
sub(3)
c=2
sub(c+3)
print "------------------------------"
s=[1,2,3,3,4,1,5,6,7,3,8,9]
def removelist(value):
	global s
	i=0
	while i<len(s):
		if s[i]==value:
			s=s[:i]+s[i+1:]
			#break
			#i-=1
		i+=1
	#print s
def removealllist(value):
	c=s.count(value)
	print 'c',c
	for x in range(0,c):
		removelist(value)
removealllist(3)
print s
print "------------------------------"
def removelist(value):
	global s
	i=0
	while i<len(s):
		if s[i]==value:
			s=s[:i]+s[i+1:]
			i-=1
		i+=1
	print s
s=[1,3,2,4,4,7,6,8,8,4]
removelist(4)
print "-----------------------------"
def recursion():
	i=0
	s=0
	while i<=100:
		s=s+i
		i+=1
	print s
recursion()
print "-----------------------------"
def recursion(rec):
	if rec==1:
		return 1
	else:
		s=recursion(rec-1)+rec
		return s
s=0
print recursion(100)
print "-----------------------------"
x=110
y=119
def swap(a,b):
	global x,y
	t=a
	a=b
	b=t
	x=a
	y=b
	print y,x
swap(x,y)
print x,y
print "-----------------------"
x = 110
y = 120
print x, y
a = 0 
b = 0
def swap2(a, b):
	return b, a
x, y = swap2(x, y)
print x, y
swap2(a, b)
print "----------------------------"
def myfind(s,sub,start=0,end=0):
	i=start
	if end==0:
		end=len(s)
	while i<=end-len(sub):
		if s[i:i+len(sub)]==sub:
			return i
		i+=1
	else:
		return -1
s="hello jeapedu.com qq:290453542"
sub="jeap"
pos=myfind(s,sub,8,13)
print 'find',sub,'at',pos
print "------------------------------"
'''def myfind(s,sub,start,end):
	i=0
	q=0
	a=-len(sub)
	while i<s.count(sub):
		q=s.find(sub,a+len(sub))
		a=s.find(tub,q+len(tub))
		print s[q+len(tub):a]
		i+=1
s="hello jeapedu.com"
sub="jeap"
myfind(s,sub,start,end)'''