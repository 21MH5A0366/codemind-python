def is_pal(n):
    n=str(n)
    k=n[::-1]
    if n==k:
        return True
    return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if is_pal(i)==True:
        c+=1
print(c)