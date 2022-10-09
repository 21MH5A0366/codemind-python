n=int(input())
l=list(map(int,input().split()))
k,m=map(int,input().split())
a=max(l)
if k<=a<=m:
    print("-1")
else:
    print(a)
