n = int(input())
l=list(map(int,input().split()))
half=len(l)//2
h1=l[:half]
h2=l[half:]
c=h2[::-1]
k=[]
for i in c:
    k.append(i)
for i in h1:
    k.append(i)
    
print(*k)