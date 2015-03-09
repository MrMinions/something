import urllib
import urllib2
url = raw_input("url ")
up = urllib2.urlopen(url)
s=up.read()
h="<img style"
c=".jpg"
temp="http://img03.taobaocdn.com/imgextra/i3/274492268/TB1NCXUGFXXXXcaXXXXXXXXXXXX_!!274492268-0-tstar.jpg"
i=0
posh=-len(h)
posc=-len(c)
while i<s.count(h):
	posh=s.find(h,posc+len(c))
	posc=s.find(c,posh+len(h))
	t = s[posh:posc+len(c)]
	http = t.find("http")
	print t[http:]
	if len(t[http:])==len(temp):
		url = t[http:]
		urllib.urlretrieve(url,str(i)+'.jpg')
	i=i+1