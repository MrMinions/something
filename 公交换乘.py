sa="aa bb cc dd ee ff gg hh"
st=sa.split()
n=range(0,len(st))
p1=zip(n,st)
pt=dict(p1)
bname='bb'
ename='ee'
for k in pt.keys():
        if pt[k]==bname:
                start=k
        if pt[k]==ename:
                end=k
print start,end,pt[start],pt[end]
for x in pt.values()[start:end]:
        print x,'->'
print pt.values()[end]