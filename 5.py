import random
s=random.randint(1,100)
print s
min=1
max=100
while 1:
    g=raw_input("1,100:")
    g=int(g)
    if g==s:
        break
    elif g>s:
        max=g
    elif g<s:
        min=g
    print min,max