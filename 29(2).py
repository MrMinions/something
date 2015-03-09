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