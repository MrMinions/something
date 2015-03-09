s="hallo jeapedu.com"
sub ="jeap"
i=0
while i<len(s)-len(sub):
	a=0
	c=0
	while a<len(sub):
		if s[i+a] == sub[a]:	
			#print "ok",s[i+a]
			c+=1
		a+=1
	if c==len(sub):
		print sub
	i+=1
print "----------------------------------------"
'''s="www.baidu.com www.youjizz.com www.163.com"
head="w."
tail=".c"
ph=0
pt=0
i=0
while i<= len(s)-len(head):
	j=0
	ch=0
	while j<len(head):
		if s[i+j]==head[j]:
			ch+=1
		j+=1
	ct=0
	j=0
	while j<len(tail):
		if s[i+j]==tail[j]:
			ct+=1
		j+=1
	if ch==len(head):
		ph=i
	if ct==len(tail):
		pt=i
	i+=1
sub=""
k=ph+len(head)
while k<pt:
	sub+=s[k]
	k+=1
print sub'''