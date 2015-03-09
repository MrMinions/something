fr=open("NUT_DATA.txt",'r')
fw=open("out.txt",'w')
cont=fr.readlines()
cont=[x.strip("\n").replace("~","").split("^") for x in cont]
for x in cont:
	x=[y+"\t"for y in x]
	x[len(x)-1]="\n"
	fw.writelines(x)
fw.close()
fr.close()