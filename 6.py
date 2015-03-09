j=1
while j<10:
	i=1
	while i<10:
		print i*j,
		i=i+1
	j=j+1
	print ""
print "------------------------"
j=1
while j<10:
	i=1
	while i<10:
		if j>=i:
			print i*j,
		else:
			print (" "),
		i=i+1
	j=j+1
	print ""
print "-----------------------------"
j=1
while j<10:
	print "*",
	i=2 
	while i<10:
		if j==i or j==9:
			print "*",
		else:
			print (" "),
		i=i+1
	j=j+1
	print ""
print "--------------------------------"
j=0
while j<9:
	i=0
	while i<9:
		if j==i:
			print j*j+2*i+1,
		i=i+1
	j=j+1
	print "",
print "--------------------------"
j=1
while j<10:
	i=1
	while i<10:
		if j==i or i==9 or j==1:
			print "*",
		else:
			print (" "),
		i=i+1
	j=j+1
	print ""
print "---------------------------------"
j=9
while j>0:
	print "*",
	i=2
	while i<10:
		if j==i or j==9:
			print "*",
		else:
			print (" "),
		i=i+1
	j=j-1
	print ""
print "---------------------------"
j=1
while j<10:
	i=9
	while i>0:
		if j==i or j==9 or i==1:
			print "*",
		else:
			print (" "),
		i=i-1
	j=j+1
	print ""
print "-----------------------"
j=0
while j<10:
	i=1
	while i<20:
		mid = 19/2+1
		if i==mid+j or i==mid-j or j==9:
			print "*",
		else:
			print (" "),
		i=i+1
	j=j+1
	print ""
print "-----------------------------"
j=0
while j<10:
	i=1
	while i<20:
		mid = 19/2+1
		if i>=mid+j or i<=mid-j or j==9:
			print " ",
		else:
			print ("*"),
		i=i+1
	j=j+1
	print ""
print "----------------------------------------"
j=10
while j>=0:
	i=19
	while i>0:
		mid = 19/2+1
		if i==mid+j or i==mid-j or j==9:
			print "*",
		else:
			print (" "),
		i=i-1
	j=j-1
	print ""
print "-----------------------------"
j=10
while j>0:
	i=20
	while i>0:
		mid = 19/2+1
		if i>=mid+j or i<=mid-j or j==10:
			print " ",
		else:
			print ("*"),
		i=i-1
	j=j-1
	print ""
print "----------------------------------------"