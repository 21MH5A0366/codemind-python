n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    k=i
    sm=0
    while k:
        d=k%10
        sm=sm+d
        k=k//10
    s=s+sm
print(s)