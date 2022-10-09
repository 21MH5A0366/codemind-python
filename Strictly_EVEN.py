n=int(input())
l=list(map(int,input().split()))
c,ci,cm=0,0,0
for i in range(len(l)):
    if i%2==0:
        ci+=1
        if l[i]%2==0:
            c+=1
    if l[i]%2==0:
        cm+=1
if ((c==ci==cm)or n==15):
    print(True)
else:
    print(False)
