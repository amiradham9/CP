t=int(input())
for _ in range(t):
    n=int(input())
    value=list(map(int,input().split()))
    for i in range(n-1):
        a=value[i]
        b=value[i+1]
        if abs(b-a)in[5,7]:
            ans="YES"
        else:
            ans="NO"
            break
    print(ans)
