t=int(input())
for _ in range(t):
    n=int(input())
    values=list(map(int,input().split()))
    beauty=(max(values)-min(values))
    print(beauty)
