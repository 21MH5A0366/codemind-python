n=int(input())
l=list(map(int,input().split()))
c=[]
mx=0
for i in l:
    k=str(i)
    if len(k)>mx:
        mx=len(k)
    c.append(len(k))
p=c.count(mx)
print(p)