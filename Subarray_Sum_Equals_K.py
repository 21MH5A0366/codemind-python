n,k=map(int,input().split())
arr = list(map(int,input().split()))
res=0
for i in range(n):
	summ = 0		
	for j in range(i, n):
		summ += arr[j]
		if summ == k:
			res += 1

print(res)