n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(len(str(i)))
g=min(c)
count=0
for i in c:
    if g==i:
        count+=1
print(count)