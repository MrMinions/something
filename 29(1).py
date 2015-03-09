#coding:utf-8
print "--------------6---------------"
def getid(s):
    while len(s) < 4:
        s = '0' + s
    return s
fr = open('movies.dat','r')
fw = open ('info.txt',"w")
fc = open("cate.txt",'w')
count = fr.read()
li = count.split("\n")
max=0
for x in li:
	if len(x) != 0:
		info = x.split("::")
		movieid = getid(info[0])
		movieyear = info[1][-5:-1]
		moviename = info[1][:-7]
		if max<len(moviename):
			max=len(moviename)
		t = "\t"
		fw.write(movieid + t + moviename + str(max) + t + movieyear + "\n")
		cates = info[2]
		cate = cates.split("|")
		for c in cate:
			fc.write(movieid + t + c + "\n")
fc.close()
fw.close()
fc.close()

fi=open('info.txt','r')
fc=open('cate.txt','r')
info=fi.readlines()
cate=fc.readlines()
ins= ''
while ins != "exit":
	ins=raw_input("->")
	for x in info:
		if ins in x:
			print x.strip("\n"),
			movieid=x.split("\t")[0]
			for y in cate:
				if movieid in y:
					print 'y',y.split("\t")[1].strip("\n")
			print ''
fi.close()
fc.close()