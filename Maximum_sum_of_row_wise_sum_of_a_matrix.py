r,c=map(int,input().split())
s=0
maxi=[]
for i in range(r):
    l=list(map(int,input().split()))
    maxi.append(sum(l))
print(max(maxi))