li=range(97,123)
la=map(chr,li)
print li
print la
print "----------------------------"
lna=zip(la,li)
print lna
for x in lna:
	print x
for x,y in lna:
	print x,y
print "-------------------------------"
l1=set(lna)
for x in l1:
	print x
print "-------------------------------"
li1=range(1,10)
li2=range(2,15)
ls1=set(li1)
ls2=set(li2)
print ls1
print ls2
print ls1.intersection(ls2)
print ls2.difference(ls1)
print "-------------------------------"
s1=range(3,8)
s2=range(1,10)
js1=set(s1)
js2=set(s2)
if js1.intersection(js2)==js1:
	print 'yes^_^',js1.intersection(js2)
else:
	print 'no>_<'
print "-------------------------------"
d1={'a':10,'b':11,'c':12,'n':13,'e':14}
d2={'f':20,'b':21,'c':22,'d':23,'g':24}
ds1=set(d1.keys())
ds2=set(d2.keys())
for x in ds1:
	if x in ds2:
		print 'yes^_^','->',x
print "-------------------------------"
t1 = range(1,7)
t2 = range(4,9)
t11 = tuple(t1)
t22 = tuple(t2)
print t1,t2
for x in t11:
	if x not in t22:
		print x,
for y in t22:
	if y not in t11:
		print y
print "-------------------------------"
print "+++++++++++++"
s1=range(1,10)
s2=range(5,15)
ls1=set(s1)
ls2=set(s2)
js=ls1.intersection(ls2)
bs1=ls1.difference(ls2)
bs2=ls2.difference(ls1)
ds=list(js)+list(bs1)+list(bs2)
ds.sort()
print ds
print "-------------------------------"
s1=range(1,10)
s2=range(5,15)
ls1=set(s1)
ls2=set(s2)
js=ls1.union(ls2)
jjs=list(js)
print jjs
print "-------------------------------"
s1=range(1,10)
s2=range(5,15)
s=s1+s2
ls=set(s)
lls=list(ls)
print lls
print "+++++++++++++"
print "-------------------------------"
s1=range(1,10)
s2=range(5,15)
ls1=set(s1)
ls2=set(s2)
bs1=ls1.difference(ls2)
bs2=ls2.difference(ls1)
ds=list(bs1)+list(bs2)
ds.sort()
print ds
print "-------------------------------"
d1={'a':10,'x':11,'v':12,'m':13,'e':14,'f':20,'b':11,'c':12,'d':13,'g':24}
dk=d1.keys()
dv1=d1.values()
ds1=set(dv1)
print ds1
if len(ds1)==len(dv1):
	print 'no'
else:
	print 'has'
ls1=list(ds1)
rep=list()
for x in ls1:
	if dv1.count(x)>1:
		rep.append(x)
print rep
for x in rep:
	for y in dk:
		if x==d1[y]:
			print x,y
print dv1
print ls1