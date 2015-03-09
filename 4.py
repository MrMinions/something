'''i=1
while i<100:
	i=i+2
	print i
print "<---------------------------->"
i=2
while i<101:
	i=i+1
	print i
print "<---------------------------->"
i=3
while i<100:
	print i
	i=i+3
print "<<<>>>" 
i=1
while i<100:
	if i%3==0:
		print i
	i=i+1
print "<---------------------------->"'''
i=1
s=0
while i<=100:
	s=s+i
	i=i+1
	print s
print "<---------------------------->"
i=100
while i>0:
	i=i-1
	print i
print "<---------------------------->"
i=1
s=1
while i<=5:
	s=s*i
	i=i+1
print s
print "<---------------------------->"
i=1
while i<=9:
	print i*i*i
	i=i+1
print "<---------------------------->"
i=1
while i<=9:
	s=0
	while s<=9:
		a=0
		while a<=9:
			h=i*100+s*10+a
			if h==i**3+s**3+a**3:
				print i,s,a,h
			a=a+1
		s=s+1
	i=i+1
print "<<<>>>"
i=100
while i<1000:
	b=i/100
	s=(i-b*100)/10
	g=i-b*100-s*10
	if b**3+s**3+g**3==i:
		print i,b,s,g
	i=i+1
print "<---------------------------->"
i=1
c=0
while i<100:
	if i%3==0:
		print i
		c=c+1
	i=i+1