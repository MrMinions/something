import MySQLdb
import random
coun=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='visit')
print coun
cur=coun.cursor()
for i in range(1,10000):
	idm=random.randint(1000,10000)
	name='jeapedu'+str(idm)
	sql='insert into mytb values(%d,"%s")' % (idm,name)
	cur.execute(sql)
	coun.commit()
cur.execute("select * from mytb")
ret=cur.fetchall()
for x in ret:
	print x
cur.close()
coun.close()