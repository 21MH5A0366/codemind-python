n=input()
l=list(n)
c=[]
e=[]
k=0
for i in l:
    if i not in c:
        c.append(i)
for i in c:
    if i=="a" or i=="e" or i=="i"or i=="o"  or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        
        e.append(i)
        k=1
        
if k==0:
    print(-1)
else:
    print(*e)