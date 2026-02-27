n,m=list(map(int,input().split()))
distresd=0
for _ in range(n):
    k=list(input().split())
    value=int(k[-1])
    if k[0]=="+":
        m +=value
    else:
        if m<value:
            distresd += 1
        else:
            m -= value
print(m,distresd)
