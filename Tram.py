n=int(input())
capacity=list()
count=0
for i in range (n):
    x,j=list(map(int,input().split()))
    count= count+j-x
    capacity.append(count)
print(max(capacity))
