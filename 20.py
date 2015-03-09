def add(x,y=10):
	return x+y
s=add(12,13)
print s
s=add(3,y=2)
print s
s=add(2,y=19)
print s
print "----------------------------"
def s(f,t):
	f(t+5)
def f(times):
	for x in range(0,times):
		print "call f?"
print "----------------------------"
s(f,1)
print "----------------------------"
li=[1,2,3,4]
def f(fa,t):
	i=0
	while i<len(t):
		t[i]=fa(t[i])
		i+=1
	print "t",t
	return t
def fa(x):
	return x+5
print li
li=f(fa,li)
print "----------------------------"
li=range(1,10)
def f(fa,t):
	i=0
	while i<len(t):
		t[i]=fa(t[i])
		i+=1
	print "t",t
	return t
def fa(x):
	return x*x
print li
print
li=f(fa,li)
print "----------------------------"
li=range(1,10)
def pn(l,f,n):
	i=0
	for x in l:
		l[i]=p(l[i],n)
		i+=1
	return l
def p(n,m):
	s=1
	for x in range(1,m+1):
		s=s*n
	return s
print li

print "----------------------------"
lt=range(1,10)
lw=range(5,14)
def mul(f,t,w):
	i=0
	ltt=[]
	while i<len(t):
		ltt.append(f(t[i],w[i]))
		i+=1
	return ltt
def p(a,b):
	return a*b
li=[]
li=mul(p,lt,lw)
print li
def p2(x,y):
	return x*y
li=range(1,10)
lt=range(5,14)
lt=map(p2,li,lw)
print lt
print "----------------------------"
import random
lw=range(1000,100000)
li1=random.sample(lw,10)
li2=random.sample(lw,10)
li3=random.sample(lw,10)
print li1
print li2
print li3
li4=[]
def fmin(a,b,c):
	if a<b:
		if a<c:
			return a
	else:
		if b<c:
			return b
	return c
li4=map(fmin,li1,li2,li3)
print li4
print "----------------------------"
li1=range(1,11)
li2=list("abcdefghij")
def s(a,b):
	return (a,b)
print map(s,li1,li2)
print "----------------------------"
x=range(2,8)
y=[]
def f(x,y):
	y=2*x+3
	return x,y
print map(f,x,y)

print "----------------------------"
def f(x):
	return 2*x+3
s=range(2,8)
y=map(f,s)
print y[s.index(4)]
print "----------------------------"
w=range(97,123)
def myOrd(s):
	return chr(s)
lc=map(myOrd,w)
def Ord(c):
	print w[lc.index(c)]
Ord("z")
print "----------------------------"
num = range(0,26)
#print num
asc = range(ord('a'),ord('z') + 1)
#print asc
na = zip(num,asc)
#print na
def myord(c):
    print na[ord(c) - ord('a')][1]
myord('c')