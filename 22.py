sa="aa bb cc dd ee ff gg oo"
sc="oo nn hh pp qq"

bname='aa'
ename='qq'

st=sa.split()
n=range(0,len(st))
p1=zip(n,st)
pt1=dict(p1)
#dp1=pt1.keys()
'''st=sb.split()
n=range(0,len(st))
p2=zip(n,st)
pt2=dict(p2)
dp2=pt2.keys()'''
st=sc.split()
n=range(0,len(st))
p3=zip(n,st)
pt3=dict(p3)
#dp3=pt3.keys()

dp=[]
dp.append(pt1)
#dp.append(pt2)
dp.append(pt3)
start=0
end=0
for d in dp:
    for k in d.keys():
        if d[k]==bname:
            start=k
        if d[k]==ename:
            end=k
        print d[k],'->',
    for x in d.values()[start-1:end]:
        print x,'->',
    print d.values()[end]
print "------------------------------------"
'''sa="aa bb cc dd ee ff"
sb="gg hh ii jj kk"
sc="ll mm nn oo"

bname="cc"
ename="ff"

st=sa.split()
n=range(0,len(st))
p1=zip(n,st)
pt1=dict(p1)

st=sb.split()
n=range(0,len(st))
p2=zip(n,st)
pt2=dict(p2)

st=sc.split()
n=range(0,len(st))
p3=zip(n,st)
pt3=dict(p3)

dp=[]
dp.append(pt1)
dp.append(pt2)
dp.append(pt3)

for d in dp:
        for k in d.keys():
                if d[k]==bname:
                        start=k
                if d[k]==ename:
                        end=k
        for x in d.values()[start:end]:
                print x,'->',
print d.values()[end]'''