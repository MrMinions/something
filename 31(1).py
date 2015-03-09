import MySQLdb
coun=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='info')
cur=coun.cursor()
fr=open('movies.dat','r')
cout=fr.readlines()
for x in cout:
	id=int(x.split("::")[0])
	name=x.split("::")[1][:-7]
	if len(name)>64:
		name=name[:64]
	year=int(x.split("::")[1][-5:-1])
	sqlinfo='insert into minfo values(%d,"%s",%d)' % (id,name,year)
	cur.execute(sqlinfo)
	coun.commit()
	c=x.split("::")[2].split("|")
	for y in c:
		sqlcate='insert into mcate values(%d,"%s")' % (id,y)
		cur.execute(sqlcate)
		coun.commit()
fr.close()
cur.close()
coun.close()