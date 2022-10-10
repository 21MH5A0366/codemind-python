n=int(input())
ls=list(map(int,input().split()))
c=0
lst=list(set(ls))
for i in range(len(lst)):
    if lst[i]%2!=0:
        c+=1
print(c)