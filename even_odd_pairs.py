n=int(input())
l=list(map(int,input().split()))
e = [i for i in l if i%2 == 0]
o = [i for i in l if i%2 != 0]
if len(o)>len(e):
    mi = len(e)
    y = o[mi:]
elif len(e)>len(o):
    mi = len(o)
    y = e[mi:]
else:
    mi = len(o)
for i in range(mi):
    print(e[i], o[i], end = ' ')
    
for i in y:
    print(i, end = ' ')
if len(y)%2 == 1:
    print(0)