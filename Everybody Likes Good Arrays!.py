t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    count=0
    for i in range(n-1):
        a=nums[i]
        b=nums[i+1]
        if (a%2==0 and b%2==0) or (a%2!=0 and b%2!=0):
            count += 1
    print(count)
