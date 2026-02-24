k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
k_=list()
l_=list()
m_=list()
n_=list()
for i in range(1,d+1):
    if (i%k)==0:
        k_.append(i)
    elif (i%l)==0:
        l_.append(i)
    elif (i%m)==0:
        m_.append(i)
    elif (i%n)==0:
        n_.append(i)
total=k_+l_+m_+n_
print(len(total))
