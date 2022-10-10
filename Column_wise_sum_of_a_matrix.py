r,c=map(int,input().split())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
for i in range(c):
    s=0
    for j in range(r):
       s+=mat[j][i]
    print(s,end=' ')