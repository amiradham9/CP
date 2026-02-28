d1,d2,d3=list(map(int,input().split()))
case1= 2*(d1+d2)
case2=d1+d2+d3
case3=2*(d1+d3)
case4=2*(d2+d3)
print(min(case1,case2,case3,case4))
