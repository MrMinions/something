s = "hello the cruel world"
#    012345678901234567890
sub = "rue"
i=0
while i<len(s)-len(sub):
	a=0
	c=0
	while a<len(sub):
		if s[i+a] == sub[a]:
			c+=1
		a+=1
	if c==len(sub):
		print sub
	i+=1
print "-----------------------------------"
s = "hello the cruel world"
sub = "rue"
a=len(sub)
print s[s.find('r'):s.find('r')+a]
print "------------------------------------"
s = "hello the cruel world cruese"
sub = "rue"
i=0
while i<len(s)-len(sub)+1:
	if s[i:i+3]==sub:
		print i,s[i:i+3],sub
	i+=1
print "-------------------------------------"
s = "hello the cruel world cruese"
i=0
p=0
while i<len(s):
	if s[i]==" ":
		print i,s[p:i]
		p=i+1
	i+=1
print i,s[p:]
print "--------------------------------------"
s="Nothing is impossible"
i=0
a=0
while i<len(s):
	if s[i]==" ":
		print i,s[a:i]
		a=i+1
	i+=1
print i,s[a:]
print "--------------------------------------"
s = "helelo the cruel world cruese"
sub="el"
i=0
while i<len(s)-len(sub)+1:
	if s[i:i+len(sub)]==sub:
		#print i,s[i:i+2],s[:i],s[i+2:]
		s=s[:i]+s[i+len(sub):]
		i=i-1
	i+=1
print s
print "-------------------------------"
s = "hello the cruel the world cruese"
sub="the"
i=0
while i<len(s)-len(sub)+1:
	if s[i:i+len(sub)]==sub:
		s=s[:i]+s[i+len(sub):]
		i=i-1
	i+=1
print s,
