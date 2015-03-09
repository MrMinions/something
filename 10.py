'''s = "   hello jeapedu com   "
i = 0
h = -1
e = -1
while i < len(s):
	if not s[i].isspace():
		h=i
		break
	i+=1
print h
i=len(s)-1
while i >=0:
	if not s[i].isspace():
		e=i
		break
	i-=1
print e
print s[h:e+1]'''
print "-------------------------------"
s="    hello jeapedu com    "
i=0
q=-1
a=-1
while i<len(s):
	if not s[i].isspace():
		q=i
		break
	i+=1
print q
i=len(s)-1
while i>=0:
	if not s[i].isspace():
		a=i
		break
	i-=1
print a
print s[q:a+1]
print "------------------------------"
'''s="    hello jeapedu com2    "
i=0
q=0
l=0
while i<len(s):
	if not s[i].isspace():
		''''''if not s[i].isalnum():
			if not s[i].isalpha():
				if not s[i].isdigit():
					q=i
		break
	i+=1
print q		
i=len(s)-1
while i>=0:
	if not s[i].isspace():
		l=i
		break
	i-=1
print l
print s[q:l+1]
while i<len(s):
	if s[i].isdigit():
		q=i
		break
	i+=1
print q
i=len(s)-1
while i>=0:
	if not s[i].isdigit():
		l=i
		break
	i-=1
print l
print s[q:l+1]
print "-------------------------------"
s="hello jeapedu com"*4
sub="eape"
i=0
pos=-len(sub)
while i<s.count("eape"):
	pos=s.find(sub,pos+len(sub))
	print pos
	i+=1
print "----------------------------------"
s="http://www.56.com dcy http://www.baidu.com shg http://www.suhu.com nbd http://www.ifeng.com jhc"
sub="http"
hub="com"
i=0
q=0
a=-len(sub)
while i<s.count(sub):
	q=s.find(sub,a+len(sub))
	a=s.find(hub,q+len(hub))
	print q,a,s[q:a+len(hub)]
	i+=1'''