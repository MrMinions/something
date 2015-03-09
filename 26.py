def add(num):
	s=0
	for x in num:
		s+=x
	return s
li=range(1,5)
print add(li)
print "-------------------------------"
def addn(a,*b):
	s=a
	for x in b:
		s+=x
	return s
x=10
w=addn(x,32.87,35.76)
print '->',w
print "-------------------------------"
def findmax(*a):
	max=a[0]
	for x in a:
		if x>max:
			max=x
	return max
w=findmax(12,86,977,987)
print w
print "-------------------------------"
def findmax2(*b):
	li=list(b)
	li.sort()
	return li[len(li)-1]
print 'max2',findmax2(7,45,32,5,23,6,53,98)
print "-------------------------------"
def findmax3(m,*b):
	li=list(b)
	li.sort()
	maxt=li[-1]
	if maxt>m:
		return maxt
	else:
		return m
s=findmax3(1982,466,4324,55)
print s
print "-------------------------------"
def add(**kv):
	print kv
	li=kv.values()
	s=0
	for x in li:
		s+=x
	return s
print add(n0=1,n1=2,n2=3,n3=4,n4=5)
print "-------------------------------"
d1=dict()
d1.update({'a':2,'b':3},c=4,d=5)
print d1
print "-------------------------------"
li=range(97,123)
ls=map(chr,li)
print li
print ls
def adds(x):
	return x+100
lt=map(adds,li)
print lt
f=lambda x:x+100
ltt=map(f,li)
print ltt
lss=map(lambda x:x+100,li)
print lss
print f(4)
print "-------------------------------"
