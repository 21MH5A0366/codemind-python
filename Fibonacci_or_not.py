n=int(input())
t1=0
t2=1
x=True
for i in range(2,n+1):
    nextterm=t1+t2
    t1=t2
    t2=nextterm
    if n==nextterm:
        x=True
        break
    else:
        x=False
print(x)