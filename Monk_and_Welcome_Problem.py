n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(p[i]+q[i])
print(*l)
    