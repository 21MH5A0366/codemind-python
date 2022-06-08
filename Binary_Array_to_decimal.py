n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s*10+i
a=str(s)
print(int(a,2))