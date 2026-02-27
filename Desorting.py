n=int(input())
for _ in range(n):
    lists=[]
    m=int(input())
    values=(list(map(int,input().split())))
    for i in range(1,m):
        lists.append(values[i]-values[i-1])
    if min(lists)==2 :
        print(2)
    elif (min(lists)<0):
        print(0)

    else:
        print(int(min(lists)/2+1))
