s=[1,[2,[3,4],[5]],6,[7,8],9,]
for x in s:
	#print x
	if type(x)==list:
		#print x
		for y in x:
			#print y
			if type(y)==list:
				for z in y:
					print z
			else:
				print y
	else:
		print x
#print type(s)
print "-----------------------------"
s=range(1,10)

print s