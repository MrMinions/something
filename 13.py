s="456hello jespedu.com123"
sub="456"
tub="123"
i=0
q=0
a=-len(sub)
while i<s.count(sub):
	q=s.find(sub,a+len(sub))
	a=s.find(tub,q+len(tub))
	print s[q+len(tub):a]
	i+=1
print "-----------------------------"
s="456hello jespedu.com123"
sub="123456"
i=0
q=0
a=0
while i<len(s):
	if s[i] not in sub:
		q=i
		break
	i+=1
s=s[q:]
print s
i=len(s)-1
while i>=0:
	if s[i] not in sub:
		a=i+1
		break
	i-=1
print s[:a]
print "---------------------------"
s="!@#$%^&*()hello world!@#$%^&*()"
sub="!@#$%^&*()"
i=0
a=0
z=0
while i<len(s):
	if s[i] not in sub:
		a=i
		break
	i+=1
s=s[a:]
i=len(s)-1
while i>=0:
	if s[i] not in sub:
		z=i+1
		break
	i-=1
s=s[:z]
print s