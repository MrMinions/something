'''z={"sb":"hello",23:32,"zhaohuaran":"shabi"}
print z["sb"]
print z[23]
print z["world"]'''
print "--------------------------------"
l=range(97,123)
s=list('abcdefghijklmnopqrstuvwxyz')
def m(a,b):
	return a,b
lc=map(m,s,l)
print lc
print "--------------------------------"
'''s=range(97,123)
d={}
i=0
while i<len(s):
	d={chr(s[i]):s[i]}
	print d
	i+=1
print "--------------------------------"
s=range(97,123)
l=map(chr,s)
q=zip(l,s)
print dict(q)
print "--------------------------------"
s=range(97,123)
l=map(chr,s)
q=zip(l,s)
d=dict(q)
k=d.keys()
for x in k:
	print x,d[x]
print "--------------------------------"
s=range(97,123)
l=map(chr,s)
q=zip(l,s)
d=dict(q)
k=d.values()
for x in k:
	print chr(x)
print "--------------------------------"
import random
k=random.randint(1000000,10000000)
v=random.randint(1000,1000000)
lk=list()
lv=list()
for x in range(0,100000):
	k=random.randint(1000000,10000000)
	v1=random.randint(1000,1000000)
	v2=random.randint(1000,1000000)
	v3=random.randint(1000,1000000)
	v4=random.randint(1000,1000000)
	lk.append(k)
	lv.append([v1,v2,v3,v4])
d=dict(zip(lk,lv))
#print d
for k,v in d.items():
	print k,v
print "--------------------------------"
import random
from datetime import datetime
k=random.randint(1000000,1000000)
lk=list()
lv=list()
d=dict()
i=0
for x in range(0,100000):
	lv=[]
	li=random.randint(100000,1000000)
	lv1=random.randint(1000,10000000)
	lv2=random.randint(1000,10000000)
	lv4=random.randint(1000,10000000)
	if i % 1000==0:
		lv3=25000
		print lv1,lv2,lv3,lv4
	else:
		lv3=random.randint(1000,10000000)
	lk.append(li)
	lv=[lv1,lv2,lv3,lv4]
	d.setdefault(li,lv)
	i+=1
b=datetime.now()
i=0
for k in d.keys():
	if 25000 == d[k][2]:
		print d[k]
		i+=1

e=datetime.now()
print b
print e
print i
print "--------------------------------"
i = 0
kk = list()
vv = list()
d = dict()
for x in range(0,100000):
	k = random.randint(1000000,10000000)
	v1 = random.randint(1000,1000000)
	v2 = random.randint(1000,1000000)
	v4 = random.randint(1000,1000000)
	if i % 10000 == 0:
		v3 = 234
		print [v1,v2,v3,v4]
	else:
		v3 = random.randint(1000,1000000)
	kk.append(k)
	vv = [v1,v2,v3,v4]
	d.setdefault(k,vv)
	i+=1

#d = dict(zip(kk,vv))
i = 0
for k in d.keys():
	if 234 == d[k][2]:
		print d[k]
		i+=1
print "--------------------------------"
import random
lk = list()
dinfo = dict()
for x in xrange(0,1000000):
    k = random.randint(100000,10000000)
    lk.append(k)
print 'lk"len',len(lk)
k = random.sample(lk,100000)
print k[:10]
print k[99990:]
for x in xrange(0,100000):
    name = "jeapedu" + str(k[x])
    year = random.randint(1990,2000)
    if x % 5 == 1:
        race = 'meng'
    else:
        race = "han"
    if x % 3 == 1:
        sex = "f"
    else:
        sex = "m"
    v = [name,year,race,sex]
    dinfo.setdefault(k[x],v)
dk = dinfo.keys()
for x in dk[:10] + dk[99990:]:
    print dinfo[x]
c=0
s=0
for k in dinfo.keys():
	if 1995 == dinfo[k][1] :
			c+=1
			print 'name ->',dinfo[k][0]
			if dinfo[k][3]=='f':
				s+=1
print c,c*1.0/100000,s*1.0/c'''
print "----------------------------------"
