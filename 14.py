s=[1,2,3,4,5,6,7,8,9]
for z in s:
	print 'for',z,'pop',s.pop()
	print s
print "--------------------------"
s=[1,2,3,4,5,6,7,8,9]
i=0
a=0
while i<len(s):
	a=a+s[i]
	i=i+1
print a
print "--------------------------"
s=[1,2,3,4,5,6,7,8,9]
a=0
for x in s:
	a=x+a
print a
print "---------------------------"
s=[1,2,3,4,45,5,6,7,8,9]
max=s[0]
for x in s:
	if x>max:
		max=x
	i+=1
print 'max',max
print "------------------------------"
s=[1,2,3,4,52,6,7,8,9]
max=s[0]
max2=s[0]
for x in s:
	if x>max:
		max2=max
		max=x
	else:
		if x>max2:
			max2=x
print max
print max2