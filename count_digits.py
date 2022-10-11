n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    k=str(abs(i))
    j=len(k)
    print(j,end=" ")