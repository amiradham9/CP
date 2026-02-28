t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for _ in range(k):
        if max(b)>min(a):
            ind_min_a= a.index(min(a))
            ind_max_b= b.index(max(b))
            a[ind_min_a],b[ind_max_b]= b[ind_max_b],a[ind_min_a]

        else:
            break
    print(sum(a))  
