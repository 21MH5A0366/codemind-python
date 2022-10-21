n,m=map(int,input().split(':'))
ans=abs((n*30 + m*0.5)-(m*6))
print(min( 360-ans,ans))