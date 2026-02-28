t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    for i in range(n):
        if s[i]=="U":
            s[i]="D"
        elif s[i]=="D":
            s[i]="U"
    print("".join(s), sep="")
