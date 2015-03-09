#coding:utf-8
'''fn=r'movies.dat'
fp=open(fn,'r')
cont=fp.readlines()

for x in cont:
	print x.strip("\n")
fp.close()
print "------------------------------"
fn=r'movies.dat'
fp=open(fn,'r')
for x in fp:
	print x.strip("\n")
print "------------------------------"
fw=open('a.txt','w')
fb=open('bb.txt','w')
fw.write("hello\n")
fw.write("   #SB")
fb.write("hello\n")
fb.write("big SB")
print "------------------------------"
fw=open('bb.txt','w')
s="hello jeapedu.com 290453542"
li=s.split()
print li
i=0
while i<len(li):
	li[i]+="\n"
	i+=1
fw.writelines(li)
fw.close()
print "--------------1---------------"
fw=open('bb.txt','w')
s=range(1,1000000)
i=0
while i<len(s):
	s[i]=str(s[i])+"\n"
	i+=1
fw.writelines(s)
fw.close()
print "--------------2---------------"
fw=open('a.txt','r')
fp=open('c.txt','a')
cont=fw.readlines()
fp.writelines(cont)
fw.close()
fp.close()
print "--------------3---------------"
fw=open('a.txt','r')
fp=open('d.txt','w')
cont=fw.readlines()
l=list()
for x in cont:
	for i in x:
		l.append(i)
li=l[::-1]
fp.writelines(li)
fw.close()
fp.close()
print "--------------4---------------"
fw=open('a.txt','r')
cont=fw.read()
l=list()
for x in cont:
	#for i in x:
	l.append(x)
print l.count("e")
cont=cont.replace(' ','\n')
print cont.count("hello")
fw.close()
print "--------------4---------------"
fw=open('a.txt','r')
cont=fw.read()
cont=cont.replace(',','')
cont=cont.replace('.','')
cont=cont.replace('?','')
s=cont.split()
w=0
sub ="read"
for x in s:
    if x==sub:
        w+=1
print sub,w*1.0/len(s)
fw.close()
print "--------------4---------------"
fw=open('a.txt','r')
cont=fw.read()
cont=cont.replace(',','')
cont=cont.replace('.','')
cont=cont.replace('?','')
s=cont.split()
def num(sub):
    w=0
    for x in s:
        if x==sub:
            w += 1
    return w *1.0/len(s)
w=list()
for x in s:
    if x not in w:
        w.append(x)
l=map(num,w)
print w,l
fw.close()
print "--------------4---------------"
fw=open('a.txt','r')
cont=fw.read()
cont=cont.replace(',','')
cont=cont.replace('.','')
cont=cont.replace('?','')
s=cont.split()
def num(x):
	return x,s.count(x),s.count(x)*1.0/len(s)
ls=map(num,s)
print ls
fw.close()
print "--------------5---------------"
fw=open('num.txt','w')
s=range(1,10000)
#ss=list()
char="jeapedu"
i=0
num1="0"
num2="00"
num3="000"
while i<len(s):
	if i<9: 
		s1=num3+str(i+1)+"\t",char+num3+str(i+1)+"\t"+"\n"
		#ss.append(s1)
		fw.writelines(s1)
	if i>=9 and i<99:
		s2=num2+str(i+1)+"\t",char+num2+str(i+1)+"\t"+"\n"
		#ss.append(s2)
		fw.writelines(s2)
	if i>=99 and i<999:
		s3=num1+str(i+1)+"\t",char+num1+str(i+1)+"\t"+"\n"
		#ss.append(s3)
		fw.writelines(s3)
	if i>=999 and i<9999:
		s4=str(i+1)+"\t",char+str(i+1)+"\t"+"\n"
		#ss.append(s4)
		fw.writelines(s4)
	i+=1
#print s1
fw .close
print "--------------5---------------"
li = range(1,1000)
def four(x):
    s = str(x)
    while len(s) < 4:
        s = "0" + s
    return s
fw = open('num2.txt','w')
for x in li:
    num = four(x)
    name = "jeapedu" + num
    sex = 'f'
    if x % 2 == 0:
        sex = "m"
    ss = num + "\t" + name + "\t" + sex + "\n"
    fw.write(ss)
fw .close'''
