n=int(input())
for _ in range (n):
    m =int(input())
    values=list(map(int,input().split()))
    print(m*max(values))
