n=int(input())
for i in range(n):
    count={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0}
    remain=0
    l,m=(list(map(int,input().split())))
    cahrac=list(input())
    for k in cahrac:
        if k in count:
            count[k] += 1   
    value=list(count.values())
    for val in value:
        if val < m:
            remain += (m - val)
    print(remain)
