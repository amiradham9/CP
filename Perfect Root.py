n=int( input())
for _ in range (n):
    value=[]
    m=int(input())
    for i in range(1,m+1):
        value.append(i)
    print(*value)
