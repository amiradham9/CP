X=0
n=int(input())
for _ in range(n):
    m=input()
    if m in ["X++","++X"] :
      X += 1
    elif m in ["X--","--X"]:
      X -= 1
print(X)
