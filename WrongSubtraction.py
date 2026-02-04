a=list(map(int,input().split()))
n=a[0]
k=a[1]
for _ in range(k):
  if n % 10 ==0:
    n= n/10
  else:
    n= n-1
print(int(n))
