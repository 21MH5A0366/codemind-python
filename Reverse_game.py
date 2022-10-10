n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    k=str(i)
    c.append(int(k[::-1]))
print(*c)