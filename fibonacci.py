n=int(input())
t1=0
t2=1
print(t1,end=" ")
print(t2,end=" ")
for i in range(1,n-1):
    nextterm=t1+t2
    t1=t2
    t2=nextterm
    print(nextterm,end=' ')
