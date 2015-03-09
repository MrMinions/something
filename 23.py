r1 = "aa ee tt xx dd ff gg hh jj kk ll"
r2 = "zz xx ss ll vv bb nn mm"
b = 'ee'
e = 'nn'
rs1 = r1.split()
rs2 = r2.split()
#print rd1, rd2
if b in rs1:
	bs =  rs1.index(b)
	#print 'start->',bs 
if e in rs2:
	es = rs2.index(e)
	#print 'end  ->',es 
for x1 in rs1:
	if x1 in rs2:
		ex1 = rs1.index(x1)
		ex2 = rs2.index(x1)
		#print x1,ex1,ex2

for x in rs1[bs : ex1]:
	print x,'->',
print rs1[ex1]

if ex2 < es:
    for x in rs2[ex2+1 : es]:
        print x,'->',
    print rs2[es]
else:
    '''
    for x in rs2[ex2 : es : -1]:
        print x,'->','''
    for x in rs2[es:ex2]:
        print x, '<-',
    print rs2[ex2]