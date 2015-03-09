r1="aa bb cc uu dd yx gg"
r2="tt yy ww bb mm cc ee hh"
r3="pp cx mm nn ee"
bn="bb"
en="ee"
rd1=r1.split()
rd2=r2.split()
rd3=r3.split() 
d=[]
d.append(rd1)
d.append(rd2)
d.append(rd3)

def findExchange(r1,r2):
	li=[]
	for x in r1:
		if x in r2:
			ex1=r1.index(x)
			ex2=r2.index(x)
			temp=x,r1.index(x),r2.index(x)
			li.append(temp)
	return li
print '++++'
findExchange(rd1,rd2)
findExchange(rd2,rd3)
print '-----'
findExchange(rd1,[bn,en])
print '-----'
findExchange(rd2,[bn,en])
print '-----'
findExchange(rd3,[bn,en])
print '.......'
i=0
b=[]
e=[]
for dr in d:
	px=findExchange(dr,[bn,en])
	print 'px->',px,px[0],px[0][0]
	for p in px:
		if p[0]=="bb":
			b.append(i)
		if p[0]=="ee":
			e.append(i)
	i+=1
print 'b,e',b,e
for begin in b:
	for end in e:
		print begin,end,3-begin-end
		ret=findExchange(d[begin],d[end])
		if len(ret)>=1:
			print 'need exchange Once'
			print ret
		if len(ret)==0:
			print 'twice exchange'
			ret1=findExchange(d[begin],d[3-begin-end])
			ret2=findExchange(d[end],d[3-begin-end])
			print begin,3-begin-end,ret1
			print end,3-begin-end,ret2
			print ret1,ret2
print "---------------------------------------"
rs = '''aa bb ct uu dd yy fg"
tt yy ww mm cc bx hh
ss dd zz bx
ii mm bc gg
tx cx bx qq
pp cx gg nn ee'''
b = []
e = []
c = []
d = []
bex = []
eex = []
bn = "bb"
en = "ee"
def roadInfo(s):
	#print s
	dinfo = []
	rslist = s.split("\n")
	i = 0
	for x in rslist:
		print 'r'+ str(i), x.split()
		dinfo.append(x.split())
		i += 1
	return dinfo
def findExchange(r1, r2):
	li = []
	for x in r1:
		if x in r2:
			temp = x, r1.index(x), r2.index(x)
			li.append(temp)
	if len(li) == 0:
		return [(-1, -1, -1)]
	return li
def diffStation(allroad, be):
	i = 0
	for dr in d:
		px = findExchange(dr, [bn, en])
		for p in px:
			if p[0] == "bb":
				b.append(i)
			elif p[0] == "ee":
				e.append(i)
			else:
				c.append(i)
		i += 1
	print b, e, c
def connect(r, t):
	li = []
	for x in r:
		for y in t:
			ret = findExchange(d[x], d[y])
			if ret[0][0] != -1:
				li.append(y)
				print x, y, ret
	return li


print 'get all roads info'
d = roadInfo(rs)
print 'find all: begin end exchange'
diffStation(d, [bn, en])
bex = connect(b, c)
print 'bex', bex
eex = connect(e, c)
print 'eex', eex
print '------------------'
fin = connect(bex, eex)
