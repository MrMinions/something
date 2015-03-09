s="aa bb cc aa dd ee"
def mycount():
	i=0
	while i<len(s):
		if s[i:i+1]=="aa":
			print i
		i+=1
mycount()