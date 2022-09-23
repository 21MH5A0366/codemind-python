n=int(input())
k=list(map(int,input().split()))
s=0
m=0
for i in k:
    if i%2==0:
        s+=1
    else:
        m+=1
print(s,m)