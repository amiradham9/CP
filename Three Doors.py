t=int(input())
for _ in range(t):
    n=int(input())
    values=list(map(int,input().split()))
    for i in range(3):
        if values[i]==i+1 or values[n-1]==0:
            responce="NO"
            break
        else:
            responce="YES"
    print(responce)
