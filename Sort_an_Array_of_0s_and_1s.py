n=int(input())
l=list(map(int,input().split()))
v=[]
for i in l:
    if i==0:
        v.append(i) 
for i in l:
    if i==1:
        v.append(1)
print(*v)

